import socketio
import time
import json
from datetime import datetime
from Runnable import *
from PySide6.QtCore import QObject, Signal

class FirebaseSignals(QObject):
    firebase_data_received = Signal(dict)

class FirebaseTestClient:
    firebase_signals = FirebaseSignals()
    firebase_data_received = firebase_signals.firebase_data_received

    def __init__(self, runnable_manager,  doc_id=None, server_url='http://localhost:5000'):
        self.doc_id = doc_id
        self.runnable_manager = runnable_manager
        self.server_url = server_url
        self.sio = socketio.Client()
        self.last_desktop_update = None
        self._setup_event_handlers()
    
    def _setup_event_handlers(self):
        """Setup all Socket.IO event handlers"""
        @self.sio.event
        def connect():
            print("✅ Connected to server")

        @self.sio.event
        def connection_established(data):
            print(f"✅ Connection established: {data}")

        @self.sio.event
        def document_set(data):
            print(f"✅ Document set: {data}")

        @self.sio.event
        def firebase_change(data):
            print(f"🔥 Firebase change received:")
            print(f"   Doc ID: {data['doc_id']}")
            print(f"   Timestamp: {data['timestamp']}")

            print(f"   Data: {json.dumps(data['data'], indent=2)}")
            firestore_data = data['data']
            
            # Check for circular updates using lastUpdatedBy and lastUpdatedAt
            try:
                last_updated_by = firestore_data.get("lastUpdatedBy")
                last_updated_at = firestore_data.get("lastUpdatedAt")
                
                # Skip if this update came from desktop
                if last_updated_by == "desktop":
                    print("🔁 Ignoring self-originated update (lastUpdatedBy = desktop)")
                    return
                
                # If we have a last desktop update timestamp, compare with incoming timestamp
                if self.last_desktop_update and last_updated_at:
                    # Convert Firestore timestamp to datetime for comparison
                    incoming_timestamp = self._parse_firestore_timestamp(last_updated_at)
                    
                    if incoming_timestamp and incoming_timestamp <= self.last_desktop_update:
                        print(f"🔁 Ignoring older update (incoming: {incoming_timestamp}, last desktop: {self.last_desktop_update})")
                        return
                
                # Update our last update timestamp if this is a newer change
                if last_updated_at:
                    parsed_timestamp = self._parse_firestore_timestamp(last_updated_at)
                    if parsed_timestamp:
                        self.last_desktop_update = parsed_timestamp
                        
            except (KeyError, TypeError, AttributeError) as e:
                print(f"⚠️ Error checking circular update: {e}")
                # Continue processing the update if we can't determine origin
            
            self.firebase_data_received.emit(firestore_data)
        
        @self.sio.event
        def update_confirmed(data):
            print(f"✅ Update confirmed: {data}")

        @self.sio.event
        def error(data):
            print(f"❌ Error: {data}")

        @self.sio.event
        def disconnect():
            print("❌ Disconnected from server")
            # Auto-reconnect after 3 seconds
            time.sleep(3)
            try:
                print("🔄 Attempting to reconnect...")
                self.sio.connect(self.server_url)
                # Re-set document if we have one
                if self.doc_id:
                    time.sleep(1)
                    self.set_document()
            except Exception as e:
                print(f"❌ Reconnection failed: {e}")
    
    def _parse_firestore_timestamp(self, timestamp_data):
        """Parse Firestore timestamp to datetime object"""
        try:
            if isinstance(timestamp_data, str):
                # Handle ISO string format
                return datetime.fromisoformat(timestamp_data.replace('Z', '+00:00'))
            elif isinstance(timestamp_data, dict):
                # Handle Firestore timestamp object format
                if '_seconds' in timestamp_data and '_nanoseconds' in timestamp_data:
                    return datetime.fromtimestamp(timestamp_data['_seconds'])
                elif 'seconds' in timestamp_data:
                    return datetime.fromtimestamp(timestamp_data['seconds'])
            elif hasattr(timestamp_data, 'timestamp'):
                # Handle actual Firestore Timestamp object
                return datetime.fromtimestamp(timestamp_data.timestamp())
            return None
        except (ValueError, TypeError, KeyError) as e:
            print(f"⚠️ Error parsing timestamp: {e}")
            return None
    
    def set_document_id(self, doc_id):
        """Set the document ID to monitor"""
        self.doc_id = doc_id
    
    def connect_to_server(self):
        """Connect to the server"""
        print(f"Connecting to server at {self.server_url}...")
        self.sio.connect(self.server_url)
        time.sleep(1)
    
    def set_document(self, doc_id=None):
        """Set document ID on the server"""
        if doc_id:
            self.doc_id = doc_id
        
        if not self.doc_id:
            print("❌ No document ID provided")
            return
        
        print(f"\nSetting document ID: {self.doc_id}...")
        self.sio.emit('set_document', {'doc_id': self.doc_id})
        time.sleep(2)
    
    def request_firebase_update(self, update_data):
        """Request Firebase update"""
        print("\nRequesting Firebase update...")
        
        # Add desktop identification and server timestamp
        update_data["lastUpdatedBy"] = "desktop"
        # Note: SERVER_TIMESTAMP will be handled by the server/Firebase
        # We'll use current time as approximation for our tracking
        current_time = datetime.utcnow()
        self.last_desktop_update = current_time
        
        self.sio.emit('request_firebase_update', {
            'doc_id': self.doc_id,
            'update_data': update_data
        })
        time.sleep(1)

    def listen_for_changes(self, can_listen):
        """Keep listening for Firebase changes"""
        print("\nListening for Firebase changes... (Press Ctrl+C to stop)")
        try:
            while can_listen:
                time.sleep(1)
        except Exception as e:
            print(f"somthing went: \n {e}")
        finally:
            self.disconnect_from_server()

    def disconnect_from_server(self):
        """Disconnect from server"""
        self.sio.disconnect()
    
    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def start_full_flow(self):
        """Run complete test flow"""
        try:
            print("Connect to server")
            # Connect to server
            self.connect_to_server()
            
            print("Set document")
            # Set document
            self.set_document()
            
            # Listen for changes
            runnable = Runnable(self.listen_for_changes)
            self.runnable_manager.runTask(runnable)
            # self.listen_for_changes(can_listen)
            
        except Exception as e:
            print(f"Error: {e}")

# Usage examples
if __name__ == '__main__':
    # Example 1: Set doc_id during initialization
    client = FirebaseTestClient(doc_id='SpO034BAsLJtzdyfuuq3')
    
    # Example 2: Set doc_id later
    # client = FirebaseTestClient()
    # client.set_document_id('your_document_id_here')
    # client.test_full_flow()
    
    # Example 3: Manual control
    # client = FirebaseTestClient(doc_id='okT7ZTsQEmPf2PFekMZn')
    # client.connect_to_server()
    # client.set_document()
    # client.listen_for_changes()

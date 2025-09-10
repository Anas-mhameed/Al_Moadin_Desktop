import socketio
import time
import json
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
        self.sio.emit('request_firebase_update', {
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
    # client = FirebaseTestClient(doc_id='your_doc_id')
    # client.connect_to_server()
    # client.set_document()
    # client.request_firebase_update({'city': 'Tel Aviv'})
    # client.listen_for_changes()

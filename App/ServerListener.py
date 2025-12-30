import socketio
import time
import json
from datetime import datetime, timezone
from Runnable import *
from PySide6.QtCore import QObject, Signal, Slot, QThread

class FirebaseSignals(QObject):
    firebase_force_stop_received = Signal(dict)
    firebase_audio_task_received = Signal(object)  # PlayAudioCommand object
    firebase_audio_preparation_received = Signal()  # Audio preparation signal
    audio_task_ack_needed = Signal(str, str, str)  # task_id, status, error (optional)
    request_firebase_update_signal = Signal(dict)  # Signal to request Firebase update
    firebase_settings_received = Signal(dict)  # Signal to receive settings
    firebase_adan_data_received = Signal(dict)  # Signal to receive adan data

class FirebaseTestClient:
    firebase_signals = FirebaseSignals()
    firebase_force_stop_received = firebase_signals.firebase_force_stop_received
    firebase_audio_task_received = firebase_signals.firebase_audio_task_received
    firebase_audio_preparation_received = firebase_signals.firebase_audio_preparation_received
    firebase_settings_received = firebase_signals.firebase_settings_received
    audio_task_ack_needed = firebase_signals.audio_task_ack_needed
    request_firebase_update_signal = firebase_signals.request_firebase_update_signal
    firebase_adan_data_received = firebase_signals.firebase_adan_data_received

    def __init__(self, runnable_manager, doc_id=None, server_url='http://localhost:5000'):
        self.doc_id = doc_id
        self.runnable_manager = runnable_manager
        self.server_url = server_url
        self.sio = socketio.Client()
        self.last_desktop_update = None
        self.is_listening = False
        self.active_audio_tasks = {}
        self._setup_event_handlers()
        
        # Connect internal signals to handle ACKs on background thread
        self.audio_task_ack_needed.connect(self._send_ack_on_background_thread)

        # Connect update signal to queue updates (will be processed on background thread)
        self.request_firebase_update_signal.connect(self._queue_firebase_update)

        # Queue for pending Firebase updates
        self._pending_updates = []
        self._update_lock = False
    
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

            firestore_data = data['data']
            
            # Check for circular updates using lastUpdatedBy and lastUpdatedAt
            try:
                last_updated_by = firestore_data.get("lastUpdatedBy")
                last_updated_at = firestore_data.get("lastUpdatedAt")
                
                if last_updated_by == "desktop":
                    print("🔁 Ignoring self-originated update (lastUpdatedBy = desktop)")
                    return
                
                if self.last_desktop_update and last_updated_at:
                    incoming_timestamp = self._parse_firestore_timestamp(last_updated_at)
                    if incoming_timestamp and incoming_timestamp < self.last_desktop_update:
                        print(f"🔁 Ignoring older update (incoming: {incoming_timestamp}, last desktop: {self.last_desktop_update})")
                        return
                
                if last_updated_at:
                    parsed_timestamp = self._parse_firestore_timestamp(last_updated_at)
                    if parsed_timestamp:
                        self.last_desktop_update = parsed_timestamp
                        
            except (KeyError, TypeError, AttributeError) as e:
                print(f"⚠️ Error checking circular update: {e}")
            
            # Check for force stop command
            playing_audio_metadata = firestore_data.get("playingAudioMetaData", {})
            if playing_audio_metadata.get("forceStop") == True:
                print("🛑 Force stop command received")
                self.firebase_force_stop_received.emit({"force_stop": True})
                return  # Don't process other data when force stop is received
            
            # Remove commands from firestore_data before emitting
            filtered_data = {k: v for k, v in firestore_data.items() if k != 'commands'}

            # Extract settings fields
            settings_fields = ['city', 'name', 'qudsDifferenceTime', 'summerTime', 'soundSensor', 'zigbeeDevice']
            settings_data = {k: v for k, v in filtered_data.items() if k in settings_fields}
            # Emit settings if any exist
            if settings_data:
                print(f"⚙️ Emitting settings data: {list(settings_data.keys())}")
                self.firebase_settings_received.emit(settings_data)

            remaining_data = {k: v for k, v in filtered_data.items() if k not in settings_fields}

            # Extract adan data
            adans_data = remaining_data.get("adansData", {})
            if adans_data:
                self.firebase_adan_data_received.emit(adans_data)

        @self.sio.event
        def audio_task(data):
            print(f"🎵 Audio task received:")
            print(f"   Task ID: {data.get('task_id')}")
            print(f"   File Path: {data.get('command', {}).get('filePath')}")
            print(f"   Command ID: {data.get('command', {}).get('id')}")
            
            task_id = data.get('task_id')
            command = data.get('command', {})
            file_path = command.get('filePath')
            command_id = command.get('id')
            
            # Validate required fields
            if not task_id or not file_path or not command_id:
                print(f"⚠️ Invalid audio task data")
                return
            
            # Check if file exists
            import os
            if not os.path.exists(file_path):
                print(f"⚠️ Audio file not found: {file_path}")
                return
            
            # Send received ACK immediately
            print(f"📨 Sending received ACK for task {task_id}")
            self.sio.emit('audio_ack', {
                'task_id': task_id,
                'status': 'received'
            })
            
            # Create audio command and emit signal to main thread
            from PlayAudioCommand import PlayAudioCommand
            audio_command = PlayAudioCommand(
                "FirebaseVoiceRecord", 
                file_path, 
                50, 
                adan_name=command_id,
                task_id=task_id
            )
            
            # Store task_id for completion tracking
            self.active_audio_tasks[command_id] = task_id
            
            # Emit signal to main thread for processing
            print(f"📡 Emitting audio task signal to main thread")
            self.firebase_audio_task_received.emit(audio_command)

        @self.sio.event
        def update_confirmed(data):
            print(f"✅ Update confirmed: {data}")

        @self.sio.event
        def error(data):
            print(f"❌ Error: {data}")

        @self.sio.event
        def disconnect():
            print("❌ Disconnected from server")
            if not self.is_listening:
                print("🛑 Not attempting reconnect - listener stopped")
                return

            # Reconnect logic runs on socket.io's internal thread
            time.sleep(3)
            try:
                print("🔄 Attempting to reconnect...")
                self.sio.connect(self.server_url)
                if self.doc_id:
                    time.sleep(1)
                    self.sio.emit('set_document', {'doc_id': self.doc_id})
            except Exception as e:
                print(f"❌ Reconnection failed: {e}")

        @self.sio.event
        def prepare_audio_playback(data):
            print(f"🎵 Audio playback preparation request received")
            
            # Emit signal to main thread for preparation
            print(f"📡 Emitting preparation signal to main thread")
            if hasattr(self, 'firebase_audio_preparation_received'):
                self.firebase_audio_preparation_received.emit()
            else:
                # Fallback: emit through firebase_data_received with special marker
                # self.firebase_data_received.emit({'prepare_audio_playback': True})
                pass

    def _send_ack_on_background_thread(self, task_id, status, error=""):
        """Send ACK from background thread (connected via signal)"""
        ack_data = {
            'task_id': task_id,
            'status': status
        }
        if error:
            ack_data['error'] = error
            
        print(f"📨 Sending {status} ACK for task {task_id}")
        self.sio.emit('audio_ack', ack_data)

    def notify_audio_completed(self, command_id):
        """Notify server that audio task has completed playing (called from main thread)"""
        if command_id in self.active_audio_tasks:
            task_id = self.active_audio_tasks[command_id]
            print(f"🎵 Requesting completion ACK for task {task_id} (command: {command_id})")
            
            # Use signal to send ACK from background thread
            self.audio_task_ack_needed.emit(task_id, 'completed', '')
            
            # Remove from active tasks
            del self.active_audio_tasks[command_id]
        else:
            print(f"⚠️ No active task found for command {command_id}")

    def notify_audio_cant_play(self, command_id):
        """Notify server that audio task can't be played (called from main thread)"""
        if command_id in self.active_audio_tasks:
            task_id = self.active_audio_tasks[command_id]
            print(f"🚫 Requesting can't play ACK for task {task_id} (command: {command_id})")
            
            # Use signal to send ACK from background thread
            self.audio_task_ack_needed.emit(task_id, 'cant_play', 'Audio cannot be played during adan time')
            
            # Remove from active tasks
            del self.active_audio_tasks[command_id]
        else:
            print(f"⚠️ No active task found for command {command_id}")

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
    
    def serialize(self, data):
        if isinstance(data, datetime):
            return data.isoformat()

        if isinstance(data, dict):
            return {
                k: self.serialize(v)
                for k, v in data.items()
            }

        if isinstance(data, (list, tuple)):
            return [
                self.serialize(item)
                for item in data
            ]

        return data

    def _queue_firebase_update(self, update_data):
        """Queue a Firebase update to be processed on background thread (called from main thread via signal)"""
        print(f"📥 Queuing Firebase update: {list(update_data.keys())}")
        self._pending_updates.append(update_data)

    def _process_pending_updates(self):
        """Process all pending updates (called from background thread during listen loop)"""
        while self._pending_updates:
            update_data = self._pending_updates.pop(0)
            self._do_firebase_update(update_data)

    def _do_firebase_update(self, update_data):
        """Actually perform the Firebase update (runs on background thread)"""
        try:
            print("\n📤 Sending Firebase update...")
            # Add desktop identification and server timestamp
            update_data["lastUpdatedBy"] = "desktop"
            current_time = datetime.now(timezone.utc)
            self.last_desktop_update = current_time
            update_data["lastUpdatedAt"] = current_time

            serialized_data = self.serialize(update_data)
            print(f"   Keys: {list(update_data.keys())}")

            self.sio.emit('request_firebase_update', {
                'doc_id': self.doc_id,
                'update_data': serialized_data
            })
            print("✅ Firebase update sent")
        except Exception as e:
            print(f"❌ Firebase update failed: {e}")

    def request_firebase_update(self, update_data):
        """Request Firebase update - for direct calls from background thread"""
        self._do_firebase_update(update_data)

    def listen_for_changes(self, can_listen):
        """Keep listening for Firebase changes and process pending updates"""
        print("\nListening for Firebase changes... (Press Ctrl+C to stop)")
        self.is_listening = True
        try:
            while can_listen() and self.is_listening:
                # Process any pending Firebase updates on this background thread
                self._process_pending_updates()
                time.sleep(0.1)  # Reduced sleep for faster update processing
        except Exception as e:
            print(f"Something went wrong: \n {e}")
        finally:
            # Process any remaining updates before disconnecting
            self._process_pending_updates()
            self.disconnect_from_server()

    def disconnect_from_server(self):
        """Disconnect from server"""
        print("Disconnecting from Firebase server...")
        self.is_listening = False
        try:
            if self.sio.connected:
                self.sio.disconnect()
                print("✅ Disconnected from Firebase server")
        except Exception as e:
            print(f"⚠️ Error during disconnect: {e}")

    def stop_listening(self):
        """Stop the listening loop"""
        self.is_listening = False

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def start_full_flow(self):
        """Run complete flow in background thread to avoid blocking UI"""
        def _start_flow_background(can_continue):
            try:
                print("🔗 Connecting to Firebase server (background thread)...")
                # Connect to server
                self.sio.connect(self.server_url)
                time.sleep(1)  # Wait for connection - OK on background thread

                print("📄 Setting document...")
                # Set document
                if self.doc_id:
                    self.sio.emit('set_document', {'doc_id': self.doc_id})
                    time.sleep(2)  # Wait for document set - OK on background thread

                print("👂 Starting to listen for changes...")
                # Now listen for changes (this will loop until stopped)
                self.listen_for_changes(can_continue)

            except Exception as e:
                print(f"❌ Firebase connection error: {e}")

        # Run the entire flow in a background thread
        runnable = Runnable(_start_flow_background)
        self.runnable_manager.runTask(runnable)

    def cleanup(self):
        """Clean up resources before app shutdown"""
        print("Cleaning up Firebase client...")
        self.stop_listening()
        self.disconnect_from_server()
        
        # Wait a bit for cleanup
        time.sleep(0.5)

    def handle_firestore_data(self, firestore_data):
        # Check for force stop command
        playing_audio_metadata = firestore_data.get("playingAudioMetaData", {})
        if playing_audio_metadata.get("forceStop") == True:
            print("🛑 Force stop command received")
            self.firebase_force_stop_received.emit({"force_stop": True})

    def update_force_stop_field(self, value):
        """Update forceStop field in Firestore (queued for background thread)"""
        update_data = {
            'playingAudioMetaData': {
                'forceStop': value
            }
        }
        # Queue the update to be processed on background thread
        self._queue_firebase_update(update_data)
        print(f"📝 Queued forceStop field update to {value}")

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

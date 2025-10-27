import requests
from Runnable import Runnable
from time import sleep

class ZigbeeController:

    def __init__(self, token, runnable_manager):
        
        self.runnable_manager = runnable_manager
        self.token = token
        self.entity_id = None
        self.connected = False
        self.mediator = None

        # Log initialization
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "uninitialized", "initializing", "ZigbeeController")

        self.try_to_connect()

        # get switch entity id
        self.prepare_entity()

    def is_entity_prepared(self):
        return self.entity_id != None

    def is_connected(self):
        return self.connected

    def try_to_connect(self):
        # Log connection attempt
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("zigbee_device", "home_assistant_api", "attempting_connection")
        
        # check if api is up
        url = "http://127.0.0.1:8123/api/"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type":"application/json"
        }
        
        status_code = 400

        try:
            response = requests.get(url=url, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "ZigbeeController", f"Connection exception: {str(e)}")

        if status_code == 200:
            print("API is up and running.")
            self.connected = True
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("zigbee_device", "home_assistant_api", "connected")
        else:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "ZigbeeController", f"Failed to connect to HA API - Status: {status_code}")

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator
        # Log mediator setup
        if self.mediator:
            self.mediator.log("adan_state_change", "no_mediator", "mediator_set", "ZigbeeController")

    def prepare_entity(self):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("zigbee_device", "entity_discovery", "searching_for_switches")
        
        url = "http://127.0.0.1:8123/api/states"
        
        status_code = 400
        try:
            response = requests.get(url=url, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "ZigbeeController", f"Entity discovery failed: {str(e)}")

        if status_code == 200:
            entities = response.json()
            switch_entities = [entity for entity in entities if entity["entity_id"].startswith("switch.")]
            
            if len(switch_entities) == 0:
                print("No entity found!")
                if hasattr(self, 'mediator') and self.mediator:
                    self.mediator.log("warning", "ZigbeeController", "No switch entities found")
                return
            
            self.entity_id = switch_entities[0]["entity_id"]
            print(f"successfuly found to entity {self.entity_id}")
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("zigbee_device", self.entity_id, f"entity_discovered - Found {len(switch_entities)} switches")
        else:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "ZigbeeController", f"Failed to prepare entity - Status: {status_code}")

    def turn_on_mic(self):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("zigbee_device", self.entity_id or "unknown", "attempting_mic_on")
        
        url = "http://127.0.0.1:8123/api/services/switch/turn_on"
        data = {"entity_id": self.entity_id}

        status_code = 400
        try:
            response = requests.post(url, json=data, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "ZigbeeController", f"Turn on mic failed: {str(e)}")

        if hasattr(self, 'mediator') and self.mediator:
            if status_code == 200:
                self.mediator.log("zigbee_device", self.entity_id, "mic_turned_on_success")
            else:
                self.mediator.log("error", "ZigbeeController", f"Turn on mic failed - Status: {status_code}")

        return status_code

    def turn_off_mic(self):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("zigbee_device", self.entity_id or "unknown", "attempting_mic_off")
        
        url = "http://127.0.0.1:8123/api/services/switch/turn_off"
        data = {"entity_id": self.entity_id}
        
        status_code = 400

        try:
            response = requests.post(url, json=data, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "ZigbeeController", f"Turn off mic failed: {str(e)}")

        if hasattr(self, 'mediator') and self.mediator:
            if status_code == 200:
                self.mediator.log("zigbee_device", self.entity_id, "mic_turned_off_success")
            else:
                self.mediator.log("error", "ZigbeeController", f"Turn off mic failed - Status: {status_code}")

        return status_code
    
    def enable_pairing_mode(self):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("zigbee_device", "zha_coordinator", "enabling_pairing_mode")
        
        url = "http://127.0.0.1:8123/api/services/zha/permit"
        data ={"duration": 60}

        status_code = 400

        try:
            response = requests.post(url, headers=self.headers, json=data)            
            status_code = response.status_code
        except Exception as e:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "ZigbeeController", f"Enable pairing failed: {str(e)}")

        if hasattr(self, 'mediator') and self.mediator:
            if status_code == 200:
                self.mediator.log("zigbee_device", "zha_coordinator", "pairing_mode_enabled_60s")
            else:
                self.mediator.log("error", "ZigbeeController", f"Enable pairing failed - Status: {status_code}")

        return status_code

    def connect_to_zigbee_btn_clicked(self):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "idle", "pairing_initiated", "ZigbeeController")
        
        status_code = self.enable_pairing_mode()
        if status_code == 200:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("zigbee_device", "pairing_process", "waiting_20s_for_devices")
            sleep(20)
            self.prepare_entity()

    def is_mic_on(self):
        if not self.entity_id:
            print("Entity not intialized!")
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("warning", "ZigbeeController", "Mic state check failed - Entity not initialized")
            return None

        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("zigbee_device", self.entity_id, "checking_mic_state")

        url = f"http://127.0.0.1:8123/api/states/{self.entity_id}"

        try:
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                state = response.json().get("state")
                print(f"{self.entity_id} is currently: {state}")
                if hasattr(self, 'mediator') and self.mediator:
                    self.mediator.log("zigbee_device", self.entity_id, f"mic_state_checked - Current: {state}")
                return state == "on"
            else:
                print(f"Failed to fetch state! Status code: {response.status_code}")
                if hasattr(self, 'mediator') and self.mediator:
                    self.mediator.log("error", "ZigbeeController", f"Mic state check failed - Status: {response.status_code}")
                return None
        except Exception as e:
            print(e)
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "ZigbeeController", f"Mic state check exception: {str(e)}")
            return None

    def run(self, on_off):
        if hasattr(self, 'mediator') and self.mediator:
            action = "turn_on" if on_off else "turn_off"
            self.mediator.log("zigbee_device", self.entity_id or "unknown", f"run_command_received - Action: {action}")
        
        def temp(func):
            if func():
                current_state = self.is_mic_on()
                if current_state is None:
                    print("Couldn't determine current state.")
                    if hasattr(self, 'mediator') and self.mediator:
                        self.mediator.log("warning", "ZigbeeController", "Run command aborted - Cannot determine mic state")
                    return

                if on_off and not current_state:
                    result = self.turn_on_mic()
                    if hasattr(self, 'mediator') and self.mediator:
                        self.mediator.log("zigbee_device", self.entity_id, f"mic_turn_on_executed - Result: {result}")
                elif not on_off and current_state:
                    result = self.turn_off_mic()
                    if hasattr(self, 'mediator') and self.mediator:
                        self.mediator.log("zigbee_device", self.entity_id, f"mic_turn_off_executed - Result: {result}")
                else:
                    print("No action needed. Already in desired state.")
                    if hasattr(self, 'mediator') and self.mediator:
                        desired_state = "on" if on_off else "off"
                        self.mediator.log("zigbee_device", self.entity_id, f"no_action_needed - Already {desired_state}")

        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)


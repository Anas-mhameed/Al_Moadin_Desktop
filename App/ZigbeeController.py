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

        self.try_to_connect()

        # get switch entity id
        self.prepare_entity()

    def is_entity_prepared(self):
        return self.entity_id != None

    def is_connected(self):
        return self.connected

    def try_to_connect(self):
        
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
            pass

        if status_code == 200:
            print("API is up and running.")
            self.connected = True
        else:
            pass

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def prepare_entity(self):
        
        url = "http://127.0.0.1:8123/api/states"
        
        status_code = 400
        try:
            response = requests.get(url=url, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            pass

        if status_code == 200:
            entities = response.json()
            switch_entities = [entity for entity in entities if entity["entity_id"].startswith("switch.")]
            
            if len(switch_entities) == 0:
                print("No entity found!")
                return
            
            self.entity_id = switch_entities[0]["entity_id"]
            print(f"successfuly found to entity {self.entity_id}")
        else:
            pass

    def turn_on_mic(self):
        
        url = "http://127.0.0.1:8123/api/services/switch/turn_on"
        data = {"entity_id": self.entity_id}

        status_code = 400
        try:
            response = requests.post(url, json=data, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            pass

        return status_code

    def turn_off_mic(self):
        
        url = "http://127.0.0.1:8123/api/services/switch/turn_off"
        data = {"entity_id": self.entity_id}
        
        status_code = 400

        try:
            response = requests.post(url, json=data, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            pass

        return status_code
    
    def enable_pairing_mode(self):
        
        url = "http://127.0.0.1:8123/api/services/zha/permit"
        data ={"duration": 60}

        status_code = 400

        try:
            response = requests.post(url, headers=self.headers, json=data)            
            status_code = response.status_code
        except Exception as e:
            pass

        return status_code

    def connect_to_zigbee_btn_clicked(self):
        
        status_code = self.enable_pairing_mode()
        if status_code == 200:
            sleep(20)
            self.prepare_entity()

    def is_mic_on(self):
        if not self.entity_id:
            print("Entity not intialized!")
            return None

        url = f"http://127.0.0.1:8123/api/states/{self.entity_id}"

        try:
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                state = response.json().get("state")
                print(f"{self.entity_id} is currently: {state}")
                return state == "on"
            else:
                print(f"Failed to fetch state! Status code: {response.status_code}")
                return None

        except Exception as e:
            print(e)
            return None

    def run(self, on_off):
        
        def temp(func):
            if func():
                current_state = self.is_mic_on()
                if current_state is None:
                    print("Couldn't determine current state.")
                    return

                if on_off and not current_state:
                    result = self.turn_on_mic()

                elif not on_off and current_state:
                    result = self.turn_off_mic()
                else:
                    print("No action needed. Already in desired state.")

        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)


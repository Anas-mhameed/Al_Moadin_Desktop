import requests
from Runnable import Runnable
from time import sleep

class ZigbeeController:

    def __init__(self, token, runnable_manager):
        
        self.runnable_manager = runnable_manager
        self.token = token
        self.entity_id = None

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
            print(e)

        if status_code == 200:
            print("API is up and running.")
        else:
            print("Failed to reach HA API!")
            print("Validate Token!")

        # get switch entity id
        self.prepare_entity()

    def prepare_entity(self):
        url = "http://127.0.0.1:8123/api/states"
        
        status_code = 400
        try:
            response = requests.get(url=url, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            print(e)

        if status_code == 200:
            entities = response.json()
            switch_entities = [entity for entity in entities if entity["entity_id"].startswith("switch.")]
            
            if len(switch_entities) == 0:
                print("No entities found!")
                return
            self.entity_id = switch_entities[0]["entity_id"]
        else:
            print("Failed to prepare entity!")

    def turn_on_mic(self):
        url = "http://127.0.0.1:8123/api/services/switch/turn_on"
        data = {"entity_id": self.entity_id}

        status_code = 400
        try:
            response = requests.post(url, json=data, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            print(e)

        return status_code

    def turn_off_mic(self):
        url = "http://127.0.0.1:8123/api/services/switch/turn_off"
        data = {"entity_id": self.entity_id}
        
        status_code = 400

        try:
            response = requests.post(url, json=data, headers=self.headers)
            status_code = response.status_code
        except Exception as e:
            print(e)

        return status_code
    
    def pair_new_device(self):
        url = "http://127.0.0.1:8123/api/services/zha/permit"
        data ={"duration": 60}

        status_code = 400

        try:
            response = requests.post(url, headers=self.headers, json=data)            
            status_code = response.status_code
        except Exception as e:
            print(e)

        return status_code

    def connect_to_zigbee_btn_clicked(self):
        status_code = self.pair_new_device()
        if status_code == 200:
            print("zigbee device paired successfully")
            sleep(20)
            self.prepare_entity()
        else:
            print("Failed to pair zigbee device!")

    def run(self, on_off):
        def temp(func):
            if func():
                if on_off:
                    self.turn_on_mic()
                else:
                    self.turn_off_mic()

        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)

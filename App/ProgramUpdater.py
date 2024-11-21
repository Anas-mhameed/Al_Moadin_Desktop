import requests
import subprocess
import sys
import os 


class ProgramUpdater:
    
    GITHUB_REPO = "Anas-mhameed/Al_Moadin_Program"

    def __init__(self, db_manager):
        self.database_manager = db_manager
        # pull current version from db
        self.current_version = self.database_manager.get_app_version() # Set to the current version of your app

    def get_latest_release(self):
        print("trying to get release ...")
        url = f"https://api.github.com/repos/{self.GITHUB_REPO}/releases/latest"
        try:
            response = requests.get(url)
            print(f"response status code: {response.status_code}")

            return response.json()
        
        except Exception as e:
            print(e)
            return None

    def check_for_updates(self):
        release = self.get_latest_release()
        
        if not release:
            return None

        latest_version = release["tag_name"]  # This is typically in the format "v1.1" or similar

        if latest_version != f"{self.current_version}":
            print(f"New version available: {latest_version}")
            return latest_version  # Return release details if update is available
        else:
            print("No updates available.")
            return None
    

    def download_update(self, latest_release):
        url = f"https://github.com/{self.GITHUB_REPO}/releases/download/{latest_release}/Al_moadin.exe"
        
        try:
            response = requests.get(url, stream=True)
            print(f"download process status code: {response.status_code}")
        except Exception as e:
            print(e)
            return 

        temp_filename = "Al_moadin_new_ver"

        with open(temp_filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded update to {temp_filename}")

        # update current version in db
        self.database_manager.update_app_version(latest_release)


    def trigger_update(temp_filename=""):
        # Launch the updater script and pass the temporary filename and main app's filename
        updater_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "../updater.py"))
        subprocess.Popen([sys.executable, updater_script, "Al_moadin_new_ver", "Al_moadin.exe"])
        sys.exit() 

    def run(self):
        # Check for updates
        latest_release = self.check_for_updates()

        if latest_release:
            self.download_update(latest_release)
            self.trigger_update()

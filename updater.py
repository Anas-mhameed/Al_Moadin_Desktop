import os
import shutil
import sys
import time
import subprocess

def apply_update(temp_filename, original_filename):
    try:
        # Wait briefly to ensure main app is closed
        time.sleep(5)
        
        # Replace the old version with the new one
        os.remove(original_filename)  # Remove the old file
        shutil.move(temp_filename, original_filename)  # Move the new file in place
        print("Update applied successfully.")
        
        # Restart the updated app
        subprocess.Popen([original_filename])
        print("Relaunched the updated app.")
        
    except Exception as e:
        print(f"Failed to apply update: {e}")

    sys.exit()

if __name__ == "__main__":
    temp_filename = sys.argv[1]  # Temporary filename of the downloaded update
    original_filename = sys.argv[2]  # Original filename of the app
    apply_update(temp_filename, original_filename)

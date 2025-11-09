from AppManager import AppManager
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from ResourceFile import resource_path
import uuid
from PySide6.QtGui import QIcon
import logging
from datetime import datetime
import os

# Setup logging configuration
def setup_logging():
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Configure logging
    log_filename = f"logs/adan_app_{datetime.now().strftime('%Y%m%d')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8')
        ]
    )
    
    logger = logging.getLogger('AdanApp')
    logger.info("=== Adan Application Started ===")
    logger.info(f"MAC Address: {get_mac_address()}")
    return logger

def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

def validate_license():
    current_mac = get_mac_address()
    logger = logging.getLogger('AdanApp')
    
    is_valid = (current_mac == 'E8:FF:1E:D4:32:0E') or True
    logger.info(f"License validation: {'PASSED' if is_valid else 'FAILED'} for MAC: {current_mac}")
    return is_valid

if __name__ == "__main__":
    logger = setup_logging()
    
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resources/images/mosque.png"))
    logger.info("Qt Application initialized")

    if validate_license():
        try:
            main_ui_file = resource_path("resources/ui/main_adan_window_ui.ui")
            logger.info(f"Loading UI file: {main_ui_file}")
            
            window = AppManager(main_ui_file)
            logger.info("AppManager instance created successfully")
            
            window.show()
            logger.info("Main window displayed")
            
            sys.exit(app.exec())
        except Exception as e:
            logger.error(f"Failed to start application: {str(e)}", exc_info=True)
            sys.exit(1)
    else:
        logger.warning("Application access denied - unauthorized device")
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Access Denied")
        msg_box.setText("Your device is not authorized to run this application.")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec() 
        sys.exit()

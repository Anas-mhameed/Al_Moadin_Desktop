import os
import sys

class ResourceFile:

    global resource_path
    
def resource_path(relative_path):
    """ Get the absolute path to a resource. """
    # If running as a bundled executable
    if hasattr(sys, '_MEIPASS'):
        # _MEIPASS is already pointing to the base directory (_internal)
        base_path = sys._MEIPASS
    else:
        # For normal running (not bundled)
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
    
# main_ui_file = resource_path("resources/ui/main_adan_page_ui.ui")
# print(main_ui_file)
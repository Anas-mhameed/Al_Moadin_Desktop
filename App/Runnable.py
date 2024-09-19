from PySide6.QtCore import QRunnable, QThreadPool
from time import sleep
from PySide6.QtCore import QObject, Signal

class Runnable(QRunnable):

    def __init__(self, func):
        super().__init__()
        self._is_running = True
        self.helper_func = func

    def stop(self):
        self._is_running = False

    def able_to_continue(self):
        return self._is_running

    def run(self):
        self.helper_func(self.able_to_continue)
        
        # while self._is_running:
            # if self.time_to_sleep:
            #     sleep(self.time_to_sleep)
            # self.helper_func()

class RunnableManager(QObject):

    force_stop_signal = Signal(object)

    def __init__(self): 
        super().__init__()   
        self.pool = QThreadPool.globalInstance()
        
    def runTask(self, runnable):
        self.force_stop_signal.connect(runnable.stop)
        self.pool.start(runnable)
    
    def wait_for_done(self):
        self.pool.waitForDone()

    def terminate_all_workers(self):
        self.force_stop_signal.emit(None)
    
    def active_workers(self):
        return self.pool.activeThreadCount()

# 0 => save in db
# 60 => reset ui
# duartion => turn off sound
# 30 => close ui
# 
# 
# 
from .tymer_base import WaitTask
from time import sleep

class interval(WaitTask):
    def task_interval_wrapper(self, *args, **kwargs):
        while(True):
            self.local_task(*args, **kwargs)
            sleep(self.wait)

            if not self.is_running:
                break

class timeout(WaitTask):
    def task_interval_wrapper(self, *args, **kwargs):
        pass

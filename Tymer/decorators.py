from .tymer_base import TymerBase
from time import sleep

class interval(TymerBase):
    def __init__(self, wait):
        self.wait = wait
        self.is_running = True

    def __call__(self, *args, **kwargs):
        try:
            tmp = self.task
        except:
            task_not_defined = True
        else:
            task_not_defined = False

        if len(args) == 1 and callable(args[0]) and task_not_defined:
            self.local_task = args[0]

            def task_interval_wrapper(*args, **kwargs):
                while(True):
                    self.local_task(*args, **kwargs)
                    sleep(self.wait)

                    if not self.is_running:
                        break

            super().__init__(task_interval_wrapper)

            return self
        else:
            return self.local_task(*args, **kwargs)

    def stop(self):
        self.is_running = False

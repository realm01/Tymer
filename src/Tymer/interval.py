from TymerBase import TymerBase
from time import sleep

class interval(TymerBase):
    def __init__(self, wait):
        self.wait = wait
        self.is_running = True

    def __call__(self, *args, **kwargs):
        # TODO: Check if self.task is already defined
        if len(args) == 1 and callable(args[0]):
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
            return self.task(*args, **kwargs)

    def stop(self):
        self.is_running = False

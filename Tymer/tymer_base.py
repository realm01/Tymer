from threading import Thread
from time import sleep


class TymerBase():
    def __init__(self):
        self.return_value = None
        self.is_running = False

    def __call__(self, *args, **kwargs):
        task_not_defined = self.task_defined()

        if len(args) == 1 and callable(args[0]) and task_not_defined:
            self.local_task = args[0]
            self.assign_task(self.task_interval_wrapper)

            return self
        else:
            return self.local_task(*args, **kwargs)

    def task_interval_wrapper(self, *args, **kwargs):
            pass

    def task_defined(self):
        try:
            tmp = self.task
        except:
            return True
        else:
            return False

    def assign_task(self, task):
        self.task = task

    def start(self, *args, **kwargs):
        if self.is_running:
            return

        self.thread = Thread(target=self.thread_func, args=args, kwargs=kwargs, daemon=True)
        self.is_running = True
        self.thread.start()

    def stop(self):
        self.is_running = False

    def thread_func(self, *args, **kwargs):
        self.return_value = self.task(*args, **kwargs)

class WaitTask(TymerBase):
    def __init__(self, wait):
        self.wait = wait
        super().__init__()

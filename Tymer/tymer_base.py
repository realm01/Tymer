from threading import Thread
from time import sleep

class TymerBase():
    def __init__(self, task):
        self.task = task
        self.return_value = None
        self.is_running = False

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

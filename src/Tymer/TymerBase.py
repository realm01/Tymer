from threading import Thread
from time import sleep

class TymerBase():
    def __init__(self, task):
        self.task = task
        self.return_value = None

    def start(self, *args, **kwargs):
        self.thread = Thread(target=self.thread, args=args, kwargs=kwargs, daemon=True)
        self.thread.start()

    def thread(self, *args, **kwargs):
        self.return_value = self.task(*args, **kwargs)

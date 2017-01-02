from threading import Thread
from time import sleep

class TymerBase():
    def __init__(self, task, wait=0, *args, **kwargs):
        self.task = task
        self.wait = wait
        self.args = args
        self.kwargs = kwargs
        self.return_value = None

        self.thread = Thread(target=self.thread, args=self.args, kwargs=self.kwargs)

    def start(self):
        self.thread.start()

    def thread(self):
        sleep(self.wait)
        self.return_value = self.task()

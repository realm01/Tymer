"""Here are all decorated used in client code.

The task_interval_wrapper method is the internal function which gets executed
by the thread. local_task is the actual client function."""

from .tymer_base import WaitTask
from time import sleep


class interval(WaitTask):
    """Task which runs in a loop, can be stopped."""

    def task_interval_wrapper(self, *args, **kwargs):
        while(True):
            self.local_task(*args, **kwargs)
            sleep(self.wait)

            if not self.is_running:
                break


class timeout(WaitTask):
    """Task which runs one time after a timeout."""

    def task_interval_wrapper(self, *args, **kwargs):
        sleep(self.wait)
        self.local_task(*args, **kwargs)

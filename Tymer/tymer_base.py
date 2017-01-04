"""Base classes of Tymer."""

from threading import Thread


class TymerBase():
    """Base class of all timed tasks."""

    def __init__(self):
        """Ctor of TymerBase."""
        self.return_value = None
        self.is_running = False

    def __call__(self, *args, **kwargs):
        """Gets called when executing the decorated function."""
        task_not_defined = self.task_defined()

        if len(args) == 1 and callable(args[0]) and task_not_defined:
            self.local_task = args[0]
            self.assign_task(self.task_interval_wrapper)

            return self
        else:
            return self.local_task(*args, **kwargs)

    def task_interval_wrapper(self, *args, **kwargs):
        """Actual method which gets executed in a thread."""
        pass

    def task_defined(self):
        """Check if a task is already defined."""
        try:
            tmp = self.task
        except:
            return True
        else:
            return False

    def assign_task(self, task):
        """Assign a task, as per TymerBase this is the task_interval_wrapper."""
        self.task = task

    def start(self, *args, **kwargs):
        """Start a task by running it in a thread."""
        if self.is_running:
            return

        self.thread = Thread(target=self.thread_func, args=args, kwargs=kwargs, daemon=True)
        self.is_running = True
        self.thread.start()

    def stop(self):
        """Signal the thread to terminate.

        Note that the termination depends on the implementation of
        task_interval_wrapper."""
        self.is_running = False

    def thread_func(self, *args, **kwargs):
        """This is the actual thread."""
        self.return_value = self.task(*args, **kwargs)


class WaitTask(TymerBase):
    """Base class of all tasks which needs to wait."""

    def __init__(self, wait):
        """Ctor of WaitTask."""
        self.wait = wait
        super().__init__()

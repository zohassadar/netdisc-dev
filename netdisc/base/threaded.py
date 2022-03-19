import threading
import queue
import logging
import typing
from netdisc.base import abstract
from netdisc.tools import helpers


class WorkerThread(threading.Thread):
    def __init__(
        self,
        index: int,
        task_doer: typing.Callable,
        input: queue.Queue,
        output: queue.Queue,
        timeout: int,
        *args,
        **kwargs,
    ):
        self.index = index
        self.task_doer = task_doer
        self.__name__ = f"Thread{self.index:02d} ({self.task_doer.__name__})"
        self.input = input
        self.output = output
        self.timeout = timeout
        self.finished = False
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            if self.finished:
                logging.info("Thread %s: Finished", self.index)
                break
            try:
                work = self.input.get(timeout=self.timeout)
                logging.critical(
                    "%s: %s is being called with: %s",
                    self.__name__,
                    self.task_doer.__name__,
                    work,
                )
                result = self.task_doer(work)
                self.output.put(result)
                logging.critical(
                    "%s: Work is ending",
                    self.__name__,
                )
                self.input.task_done()
            except queue.Empty:
                pass


class ThreadedQueue(abstract.QueueBase):
    def __init__(self, task_doer: typing.Callable, workers: int, worker_timeout: int):
        self.task_doer = task_doer
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()
        self.workers = workers
        self._workers = []
        for index in range(self.workers):
            worker = WorkerThread(
                index,
                task_doer,
                self.input_queue,
                self.output_queue,
                worker_timeout,
            )
            worker.start()
            self._workers.append(worker)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.workers=})"

    def __str__(self):
        return repr(self)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type:
            logging.error("Type: %s, Value: %s, Traceback: %s", type, value, traceback)
        else:
            logging.info("Normal exit condition")
        self.close()

    def close(self):
        for worker in self._workers:
            worker.finished = True
        self.input_queue = None
        self.output_queue = None

    @helpers.debugger(logging.CRITICAL)
    def put(self, *args, **kwargs):
        return self.input_queue.put(*args, **kwargs)

    @helpers.debugger(logging.CRITICAL)
    def get(self, *args, **kwargs):
        return self.output_queue.get(*args, **kwargs)

    @helpers.debugger(logging.CRITICAL)
    def empty(self):
        return self.output_queue.empty()

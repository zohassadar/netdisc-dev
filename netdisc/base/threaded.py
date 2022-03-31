import logging
import queue
import threading
import time
import typing

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class WorkerThread(threading.Thread):
    def __init__(
        self,
        worker: typing.Callable,
        timeout: int,
        index: int,
        input: queue.Queue,
        output: queue.Queue,
    ):
        super().__init__(name=f"{worker.__name__}_Thread{index:02d}")
        self.worker = worker
        self.timeout = timeout
        self.index = index
        self.input = input
        self.output = output
        self.stop = False
        logger.debug("Instantiated")

    def run(self):
        logger.debug("Running")
        while True:
            if self.stop:
                logging.info("Thread %s: Finished", self.index)
                break
            try:
                work = self.input.get(timeout=self.timeout)
            except queue.Empty:
                continue
            result = self.worker(work)
            self.output.put(result)
            self.input.task_done()


class WorkerPoolThread(threading.Thread):
    def __init__(
        self,
        worker: typing.Callable,
        timeout: int,
        max_workers: int,
    ):
        super().__init__(name=type(self).__name__)
        self.worker = worker
        self.timeout = timeout
        self.max_workers = max_workers
        self.input = queue.Queue()
        self.output = queue.Queue()
        self.stop = False
        self._workers: list[WorkerThread] = []
        for index in range(self.max_workers):
            worker = WorkerThread(
                worker=self.worker,
                timeout=self.timeout,
                index=index,
                input=self.input,
                output=self.output,
            )
            self._workers.append(worker)
        logger.debug("Instantiated")

    def __enter__(self):
        logger.debug("Starting Workers")
        for worker in self._workers:
            worker.start()
        self.start()
        return self

    def __exit__(self, *exc):
        for worker in self._workers:
            worker.stop = True
        self.stop = True
        logger.debug("Stopping Workers")

    def run(self):
        logger.debug("Starting")
        while True:
            if self.stop:
                break
            time.sleep(self.timeout)

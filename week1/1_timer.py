import time


class TimerError(Exception):
    """Costom timer exception. for now its just basic"""


class Timer:
    def __init__(self) -> None:
        self._start_time = None
        self._elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. use stop()")
        self._start_time = time.perf_counter()  # started the time

    def stop(self):
        """Save the elapsed time and re-init timer"""
        if self._start_time is None:
            raise TimerError("Timer never started, User start()")

        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self):
        """Reports the elapsed time"""
        if self._elapsed_time is None:
            raise TimerError("Timer has not been started or stopped.")
        return self._elapsed_time

    def __str__(self) -> str:
        return str(self._elapsed_time)


t = Timer()

for j in range(4, 10):
    t.start()
    n = 0
    for i in range(10**j):
        n = n + 1
    t.stop()

    print(j, t)

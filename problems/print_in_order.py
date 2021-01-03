from threading import Lock


class Foo:
    def __init__(self):
        self.first_done_lock = Lock()
        self.first_done_lock.acquire()

        self.second_done_lock = Lock()
        self.second_done_lock.acquire()

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done_lock.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        with self.first_done_lock:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.second_done_lock.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        with self.second_done_lock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()

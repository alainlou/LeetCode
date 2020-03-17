class Foo:
    def __init__(self):
        self.ord = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.ord = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.ord < 1:
            pass
        printSecond()
        self.ord = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.ord < 2:
            pass
        printThird()

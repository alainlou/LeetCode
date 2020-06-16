class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        while len(self.stack) > self.idx + 1:
            self.stack.pop(-1)
        self.stack.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.stack[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(len(self.stack) - 1, self.idx + steps)
        return self.stack[self.idx]

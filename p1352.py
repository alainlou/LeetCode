class ProductOfNumbers:

    def __init__(self):
        self.zero = -1
        self.ans = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zero = len(self.ans)
        if len(self.ans) == 0:
            self.ans.append(num)
        elif self.ans[-1] != 0:
            self.ans.append(self.ans[-1]*num)
        else:
            self.ans.append(num)

    def getProduct(self, k: int) -> int:
        if len(self.ans) - k <= self.zero:
            return 0
        elif len(self.ans) - k == self.zero+1:
            return self.ans[-1]
        return self.ans[-1]//self.ans[-k-1] if k < len(self.ans) else self.ans[-1]

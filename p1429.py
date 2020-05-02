from collections import defaultdict

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counts = defaultdict(int)
        self.pntr = 0
        self.nums = []

        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return self.nums[self.pntr] if self.pntr < len(self.nums) else -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.counts[value] += 1

        while self.pntr < len(self.nums) and self.counts[self.nums[self.pntr]] > 1:
            self.pntr += 1

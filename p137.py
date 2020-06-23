from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        for k, v in count.items():
            if v == 1:
                return k

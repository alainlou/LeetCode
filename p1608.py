class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1001):
            count = 0
            for n in nums:
                if n >= i:
                    count += 1
            if i == count:
                return i
        return -1

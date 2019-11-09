class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1
        max_count = 0
        solution = None
        for i in counts:
            if counts[i] > max_count:
                max_count = counts[i]
                solution = i
        return solution
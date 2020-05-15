class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_sum = float('-inf')
        max_candidate = 0
        min_sum = float('inf')
        min_candidate = 0
        total = 0

        for n in A:
            max_candidate = max(n, max_candidate + n)
            max_sum = max(max_sum, max_candidate)
            min_candidate = min(n, min_candidate + n)
            min_sum = min(min_sum, min_candidate)
            total += n

        return max(total - min_sum, max_sum) if total != min_sum else max_sum

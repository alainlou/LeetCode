from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        acc = 0
        ans = 0

        for n in nums:
            acc += n
            ans += counts[acc-k]
            counts[acc] += 1
            ans += 1 if acc == k else 0

        return ans

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        ans = set()

        for n in nums:
            if n+k in seen:
                ans.add((n, n+k))
            if n-k in seen:
                ans.add((n-k, n))
            seen.add(n)

        return len(ans)

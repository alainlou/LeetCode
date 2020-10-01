class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        s = set()

        for n in nums:
            s.add(n)
            while ans in s:
                ans += 1

        return ans

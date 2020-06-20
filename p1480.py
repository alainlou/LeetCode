class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        ans = []

        for n in nums:
            curr += n
            ans.append(curr)

        return ans

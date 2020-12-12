from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0]*n

        for i in range(1,n):
            left[i] += (nums[i]-nums[i-1])*(i)
            left[i] += left[i-1]

        right = [0]*n
        for i in range(n-2, -1, -1):
            right[i] += (nums[i+1]-nums[i])*(n-1-i)
            right[i] += right[i+1]

        ans = [0]*n

        for i in range(n):
            ans[i] = left[i] + right[i]

        return ans

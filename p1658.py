from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left, right = 0, 1
        curr = nums[0]
        target = sum(nums)-x

        ans = float('inf')

        if target < 0:
            return -1
        if target == 0:
            return n

        while left < n:
            if curr < target:
                if right == n:
                    break
                curr += nums[right]
                right += 1
                if curr == target:
                    ans = min(ans, n-(right-left))
            else:
                if curr == target:
                    ans = min(ans, n-(right-left))
                curr -= nums[left]
                left += 1

        return ans if ans != float('inf') else -1

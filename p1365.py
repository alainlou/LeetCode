class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for n in nums:
            count[n] += 1
        for i in range(1, 101):
            count[i] += count[i-1]
        ans = nums[:]
        for i in range(len(ans)):
            ans[i] = count[ans[i]-1] if ans[i] > 0 else 0
        return ans

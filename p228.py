class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        if n == 0:
            return []

        start = nums[0]
        curr = nums[0]
        ans = []

        for i in range(1, n):
            if nums[i] > nums[i-1]+1:
                if start == curr:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+'->'+str(curr))
                start = nums[i]
                curr = nums[i]
            else:
                curr = nums[i]

        if start == curr:
            ans.append(str(start))
        else:
            ans.append(str(start)+'->'+str(curr))

        return ans

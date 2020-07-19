class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def solve(idx, curr):
            if idx > len(nums)-1:
                ans.append(curr[:])
                return
            curr.append(nums[idx])
            solve(idx+1, curr)
            curr.pop(-1)
            solve(idx+1, curr)

        solve(0, [])

        return ans

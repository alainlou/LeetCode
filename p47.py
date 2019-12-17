class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:     
        def solve(counts, curr, ans, n):
            if len(curr) == n:
                ans.append(curr[:])
            for num in counts:
                if counts[num] > 0:
                    counts[num] -= 1
                    curr.append(num)
                    solve(counts, curr, ans, n)
                    counts[num] += 1
                    curr.pop()
        n = len(nums)
        ans = []
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        solve(counts, [], ans, n)
        return ans
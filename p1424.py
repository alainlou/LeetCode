from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        data = defaultdict(list)
        k = 0
        ans = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                data[i+j].insert(0, nums[i][j])
                k = max(k, i+j)

        for k in sorted(data.keys()):
            ans.extend(data[k])

        return ans

from heapq import heapify, heappop

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        counts = [0]*len(nums)

        for r in requests:
            counts[r[0]] += 1
            if r[1]+1 < len(counts):
                counts[r[1]+1] -= 1

        tmp = 0
        for i, c in enumerate(counts):
            tmp += c
            counts[i] = tmp

        counts.sort(reverse = True)

        ans = 0

        for i, n in enumerate(nums):
            nums[i] = -n

        heapify(nums)

        for c in counts:
            ans += heappop(nums)*c

        return -ans%(10**9+7)

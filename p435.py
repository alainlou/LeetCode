class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        ans = 0
        idx = 0

        while idx < len(intervals)-1:
            if intervals[idx][1] > intervals[idx+1][0]:
                del intervals[idx+1]
                ans += 1
            else:
                idx += 1

        return ans

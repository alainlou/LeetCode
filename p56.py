class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        idx = 1

        while idx < len(intervals):
            if intervals[idx][0] <= intervals[idx-1][1]:
                intervals[idx-1][1] = max(intervals[idx-1][1], intervals[idx][1])
                del intervals[idx]
            else:
                idx += 1

        return intervals

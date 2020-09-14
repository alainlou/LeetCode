class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        elif newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        elif newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        idx = 0
        flag = False

        while idx < len(intervals):
            if flag:
                if idx+1 < len(intervals) and intervals[idx][1] >= intervals[idx+1][0]:
                    intervals[idx][1] = max(intervals[idx][1], intervals[idx+1][1])
                    del intervals[idx+1]
                else:
                    idx += 1
            elif intervals[idx][1] >= newInterval[0]:
                if newInterval[1] < intervals[idx][0]:
                    intervals.insert(idx, newInterval)
                else:
                    intervals[idx][0] = min(intervals[idx][0], newInterval[0])
                    intervals[idx][1] = max(intervals[idx][1], newInterval[1])
                flag = True
            else:
                idx += 1

        return intervals

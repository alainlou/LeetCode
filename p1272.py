class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        while i < len(intervals):
            if toBeRemoved[0] <= intervals[i][0] and toBeRemoved[1] > intervals[i][0] and toBeRemoved[1] < intervals[i][1]:
                intervals[i][0] = toBeRemoved[1]
            elif toBeRemoved[0] > intervals[i][0] and toBeRemoved[1] < intervals[i][1]:
                intervals.append([toBeRemoved[1], intervals[i][1]])
                intervals[i][1] = toBeRemoved[0]
            elif toBeRemoved[0] > intervals[i][0] and toBeRemoved[0] < intervals[i][1] and toBeRemoved[1] >= intervals[i][1]:
                intervals[i][1] = toBeRemoved[0]
            elif toBeRemoved[0] <= intervals[i][0] and toBeRemoved[1] >= intervals[i][1]:
                del intervals[i]
                i -= 1
            i += 1
        intervals.sort()
        return intervals
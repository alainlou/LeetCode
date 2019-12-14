class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        while i < len(intervals):
            flag = False
            for j in range(i-1, -1, -1):
                if intervals[j][0] <= intervals[i][0] \
                and intervals[i][1] <= intervals[j][1]:
                    del intervals[i]
                    i -= 1                    
                    flag = True
                    break
            if flag == False:
                for k in range(i+1, len(intervals)):
                    if intervals[k][0] <= intervals[i][0] \
                    and intervals[i][1] <= intervals[k][1]:
                        del intervals[i]
                        i -= 1                        
                        break
            i += 1
        return len(intervals)
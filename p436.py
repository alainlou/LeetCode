class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        for i, e in enumerate(intervals):
            intervals[i] = e + [i]

        by_start = sorted(intervals)
        intervals.sort(key = lambda x: (x[1], x[0]))

        s = [0]
        ans = [-1]*len(intervals)

        for i in range(1, len(by_start)):
            while len(s) > 0 and by_start[i][0] >= intervals[s[0]][1]:
                ans[intervals[s.pop(0)][2]] = by_start[i][2]
            s.append(i)

        return ans

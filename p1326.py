class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [[r[0]-r[1], r[0]+r[1]] for r in enumerate(ranges)]
        intervals.sort(key=lambda x: x[0])
        idx = 1
        while idx < len(intervals):
            if intervals[idx][1] < intervals[idx-1][1]:
                del intervals[idx]
            else:
                idx += 1
        ans = 0
        end = 0
        for i in range(n+1):
            if i > end:
                best = end
                idx = 0
                while idx < len(intervals):
                    if intervals[idx][0] > end:
                        break
                    if intervals[idx][1] < best:
                        del intervals[idx]
                        continue
                    if intervals[idx][0] <= end and intervals[idx][1] > best:
                        best = intervals[idx][1]
                    idx += 1
                end = best
                ans += 1
        return ans if end >= n else -1

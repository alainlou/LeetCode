from math import sqrt

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        ans = [0, 0]
        best = float('-inf')

        for i in range(51):
            for j in range(51):
                curr = 0
                for t in towers:
                    if (i-t[0])**2 + (j-t[1])**2 <= radius**2:
                        curr += int(t[2]/(sqrt((i-t[0])**2 + (j-t[1])**2) + 1))
                if curr > best:
                    ans = [i, j]
                    best = curr

        return ans

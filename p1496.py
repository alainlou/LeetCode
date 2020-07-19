class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        curr = [0, 0]
        seen.add((0, 0))
        for p in path:
            if p == 'N':
                curr[1] -= 1
            elif p == 'S':
                curr[1] += 1
            elif p == 'E':
                curr[0] += 1
            elif p == 'W':
                curr[0] -= 1
            if (curr[0], curr[1]) in seen:
                return True
            seen.add((curr[0], curr[1]))
        return False

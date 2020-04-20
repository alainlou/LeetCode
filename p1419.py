class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counts = [0]*4
        ans = 0

        for c in croakOfFrogs:
            if c == 'c':
                counts[0] += 1
            elif c == 'r':
                counts[1] += 1
                counts[0] -= 1
                if counts[0] < 0:
                    return -1
            elif c == 'o':
                counts[2] += 1
                counts[1] -= 1
                if counts[1] < 0:
                    return -1
            elif c == 'a':
                counts[3] += 1
                counts[2] -= 1
                if counts[2] < 0:
                    return -1
            elif c == 'k':
                counts[3] -= 1
            ans = max(ans, sum(counts))

        return ans if max(counts) == 0 else -1

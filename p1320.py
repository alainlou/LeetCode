class Solution:
    def minimumDistance(self, word: str) -> int:
        memo = {}
        coord = {
            'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4), 'F': (0, 5),
            'G': (1, 0), 'H': (1, 1), 'I': (1, 2), 'J': (1, 3), 'K': (1, 4), 'L': (1, 5),
            'M': (2, 0), 'N': (2, 1), 'O': (2, 2), 'P': (2, 3), 'Q': (2, 4), 'R': (2, 5),
            'S': (3, 0), 'T': (3, 1), 'U': (3, 2), 'V': (3, 3), 'W': (3, 4), 'X': (3, 5),
            'Y': (4, 0), 'Z': (4, 1)
        }
        n = len(word)
        def get_cost(c1, c2):
            if c1 is None:
                return 0
            return abs(coord[c1][0]-coord[c2][0]) + abs(coord[c1][1]-coord[c2][1])

        def solve(i, finger1, finger2):
            if i == n:
                return 0
            if (i, finger1, finger2) in memo:
                return memo[(i, finger1, finger2)]
            ans = min(get_cost(finger1, word[i]) + solve(i+1, word[i], finger2),\
                   get_cost(finger2, word[i]) + solve(i+1, finger1, word[i]))
            memo[(i, finger1, finger2)] = ans
            return ans

        return solve(0, None, None)

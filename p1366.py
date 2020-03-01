from functools import cmp_to_key

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        ans = []
        tally = [[0]*26 for _ in range(26)]

        for vote in votes:
            for i in range(len(vote)):
                tally[i][ord(vote[i])-65] += 1

        def tiebreak(cand1, cand2):
            cand1 = ord(cand1)-65
            cand2 = ord(cand2)-65
            for i in range(n):
                if tally[i][cand1] > tally[i][cand2]:
                    return -1
                elif tally[i][cand1] < tally[i][cand2]:
                    return 1
            return 0

        i = 0
        row = 0
        while i < n:
            candidates = []
            count = float('-inf')
            for j in range(26):
                if tally[row][j] > count and chr(j+65) not in ans:
                    candidates = [chr(j+65)]
                    count = tally[row][j]
                elif tally[row][j] == count and chr(j+65) not in ans:
                    candidates.append(chr(j+65))

            candidates.sort(key=cmp_to_key(tiebreak))

            ans.extend(candidates)
            i += len(candidates)

        return "".join(ans[:n])

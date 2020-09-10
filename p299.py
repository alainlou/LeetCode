from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        counts1, counts2 = defaultdict(int), defaultdict(int)

        for i, c in enumerate(secret):
            if c == guess[i]:
                bulls += 1
            else:
                counts1[c] += 1
                counts2[guess[i]] += 1

        for k in counts1.keys():
            cows += min(counts1[k], counts2[k])

        return str(bulls) + 'A' + str(cows) + 'B'

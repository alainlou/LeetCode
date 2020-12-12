from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)

        for i in range(n):
            tmp = bobValues[i] + aliceValues[i]
            aliceValues[i] = (-tmp, aliceValues[i], i)
            bobValues[i] = (-tmp, bobValues[i], i)

        aliceValues.sort()
        bobValues.sort()

        removed = set()

        scores = [0, 0]
        i = 0

        while len(aliceValues) > 0 and len(bobValues) > 0:
            if i == 0:
                while len(aliceValues) > 0 and aliceValues[0][2] in removed:
                    aliceValues.pop(0)
                if len(aliceValues) > 0:
                    removed.add(aliceValues[0][2])
                    scores[i] += aliceValues.pop(0)[1]
            else:
                while len(bobValues) > 0 and bobValues[0][2] in removed:
                    bobValues.pop(0)
                if len(bobValues) > 0:
                    removed.add(bobValues[0][2])
                    scores[i] += bobValues.pop(0)[1]
            i += 1
            i %= 2

        return 1 if scores[0] > scores[1] else 0 if scores[0] == scores[1] else -1

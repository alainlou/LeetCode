class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(c for c in J)
        ans = 0

        for s in S:
            if s in jewels:
                ans += 1

        return ans

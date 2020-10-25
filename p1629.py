class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev = 0
        hi = 0
        ans = keysPressed[0]

        for i, t in enumerate(releaseTimes):
            if t-prev > hi:
                hi = t-prev
                ans = keysPressed[i]
            elif t-prev == hi:
                ans = max(ans, keysPressed[i])
            prev = t

        return ans

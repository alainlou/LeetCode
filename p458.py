class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = minutesToTest//minutesToDie
        i = 0
        while (n+1)**i < buckets:
            i += 1
        return i

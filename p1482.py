from functools import lru_cache

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1

        @lru_cache(None)
        def valid(day):
            count = 0
            curr = 0
            for b in bloomDay:
                if b <= day:
                    curr += 1
                else:
                    curr = 0
                if curr >= k:
                    curr = 0
                    count += 1
                if count >= m:
                    return True

        left, right = 0, 1e9+1
        mid = (left+right)//2

        while True:
            if valid(mid) and not valid(mid-1):
                return int(mid)
            elif valid(mid):
                right = mid
            else:
                left = mid+1
            mid = (left+right)//2

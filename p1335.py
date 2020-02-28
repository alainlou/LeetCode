from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        n = len(jobDifficulty)

        right = jobDifficulty[:]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i], right[i+1])

        @lru_cache(None)
        def recurse(idx, day):
            if idx == n - 1:
                return jobDifficulty[-1]
            elif idx >= n:
                return 0
            elif day == 0:
                return right[idx]
            else:
                cost = jobDifficulty[idx]
                best = cost + recurse(idx + 1, day - 1)
                for i in range(idx + 1, n - day + 1):
                    cost = max(cost, jobDifficulty[i])
                    best = min(best, cost + recurse(i + 1, day - 1))
                return best

        return recurse(0, d)

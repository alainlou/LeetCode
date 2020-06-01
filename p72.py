from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        e1, e2 = len(word1), len(word2)

        @lru_cache(None)
        def dfs(s1, s2):
            if e1-s1 == 0 or e2-s2 == 0:
                return max(e1-s1, e2-s2)

            if word1[s1] == word2[s2]:
                return dfs(s1+1, s2+1)
            return 1 + min(dfs(s1+1, s2), dfs(s1, s2+1), dfs(s1+1, s2+1))

        return dfs(0, 0)

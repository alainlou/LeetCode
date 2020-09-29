from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @lru_cache(None)
        def dfs(idx, curr):
            if idx == len(s)-1:
                return curr in word_set
            ret = False if curr not in word_set else dfs(idx+1, s[idx+1])
            curr += s[idx+1]
            ret = True if dfs(idx+1, curr) else ret
            #  we don't actually need to pop here (not "backtracking")
            return ret

        return dfs(0, s[0])

from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        st = set(wordDict)

        @lru_cache(None)
        def dfs(string):
            if string == '':
                return [[]]
            ans = []
            for i in range(1, len(string)+1):
                if string[:i] in st:
                    for lst in dfs(string[i:]):
                        ans.append([string[:i]] + lst)
            return ans

        return [' '.join(ans) for ans in dfs(s)]

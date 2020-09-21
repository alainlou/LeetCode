class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        n = len(s)

        def dfs(idx):
            if idx > n-1:
                return 0
            ans = 0
            for i in range(idx, n):
                if s[idx:i+1] not in seen:
                    seen.add(s[idx:i+1])
                    ans = max(ans, 1+dfs(i+1))
                    seen.remove(s[idx:i+1])
            return ans

        return dfs(0)

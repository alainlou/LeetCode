class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)

        @lru_cache(None)
        def dfs(start):
            if start > n-1:
                return 0

            ans = costs[0] + dfs(start+1)

            for i in range(start, n):
                if days[i]-days[start] >= 30:
                    break
                ans = min(ans, costs[2] + dfs(i+1))
                if days[i]-days[start] < 7:
                    ans = min(ans, costs[1] + dfs(i+1))

            return ans

        return dfs(0)

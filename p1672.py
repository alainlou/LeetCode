class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = float('-inf')

        for row in accounts:
            ans = max(ans, sum(row))

        return ans

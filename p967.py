class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        curr, ans = 0, []

        def dfs(idx):
            nonlocal curr
            if idx >= N:
                ans.append(curr)
                return
            if idx == 0:
                for i in range(0 if N == 1 else 1, 10):
                    curr *= 10
                    curr += i
                    dfs(idx+1)
                    curr //= 10
            else:
                if curr%10-K >= 0:
                    tmp = curr%10-K
                    curr *= 10
                    curr += tmp
                    dfs(idx+1)
                    curr //= 10
                if K != 0 and curr%10+K <= 9:
                    tmp = curr%10+K
                    curr *= 10
                    curr += tmp
                    dfs(idx+1)
                    curr //= 10

        dfs(0)
        return ans

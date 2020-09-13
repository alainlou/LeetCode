class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        curr = []

        def dfs(k, n, f):
            if k == 0:
                if n == 0:
                    ans.append(curr[:])
                return
            for i in range(f, 10):
                curr.append(i)
                dfs(k-1, n-i, i+1)
                curr.pop(-1)

        dfs(k, n, 1)

        return ans

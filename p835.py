class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)

        def calc(i, j):
            ans = 0
            for x in range(n):
                for y in range(n):
                    if 0 <= x+i < n and 0 <= y+j < n and 1 == A[x+i][y+j] == B[x][y]:
                        ans += 1
            return ans

        ans = 0

        for i in range(-n+1, n):
            for j in range(-n+1, n):
                ans = max(ans, calc(i, j))

        return ans

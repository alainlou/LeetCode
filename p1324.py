class Solution:
    def printVertically(self, s: str) -> List[str]:
        matrix = s.split()
        m = max(map(len, matrix))
        n = len(matrix)
        ans = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i < len(matrix[j]):
                    ans[i].append(matrix[j][i])
                else:
                    ans[i].append(" ")
            ans[i] = "".join(ans[i]).rstrip()
        return ans

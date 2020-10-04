class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)

        ans = [[0]*n for _ in range(m)]

        incr = 0
        arr = [[colSum[incr], incr]]
        incr += 1
        s = arr[0][0]

        for i in range(m):
            while rowSum[i] > s:
                arr.append([colSum[incr], incr])
                incr += 1
                s += arr[-1][0]
            for j, e in enumerate(arr):
                tmp = min(rowSum[i], e[0])
                ans[i][e[1]] += tmp
                arr[j][0] -= tmp
                rowSum[i] -= tmp
                s -= tmp
                if rowSum[i] == 0:
                    break

        return ans

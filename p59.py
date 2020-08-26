class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        direction = 0
        row = 0
        col = 0
        i = 1
        while i <= pow(n, 2):
            ans[row][col] = i
            i += 1
            if (direction == 0 and (col == n-1 or ans[row][col+1] != 0))\
            or (direction == 1 and (row == n-1 or ans[row+1][col] != 0))\
            or (direction == 2 and (col == 0 or ans[row][col-1] != 0))\
            or (direction == 3 and (row == 0 or ans[row-1][col] != 0)):
                direction = (direction+1)%4
            if direction == 0:
                col += 1
            elif direction == 1:
                row += 1
            elif direction == 2:
                col -= 1
            else:
                row -= 1
        return ans

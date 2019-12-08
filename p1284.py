def isZero(mat):
    for row in mat:
        for box in row:
            if box != 0:
                return False
    return True

def hashed(mat):
    h = []
    for row in mat:
        for box in row:
            h.append(str(box))
    return ''.join(h)

def flip(mat, row, col):
    mat[row][col] = 0 if mat[row][col] else 1
    if row > 0:
        mat[row-1][col] = 0 if mat[row-1][col] else 1
    if row < len(mat)-1:
        mat[row+1][col] = 0 if mat[row+1][col] else 1
    if col > 0:
        mat[row][col-1] = 0 if mat[row][col-1] else 1
    if col < len(mat[0])-1:
        mat[row][col+1] = 0 if mat[row][col+1] else 1

class Solution:
    def __init__(self):
        self.solutions = {}
        self.seen = set()
        
    def inner(self, mat):
        if hashed(mat) in self.seen:
            if hashed(mat) in self.solutions:
                return self.solutions[hashed(mat)]
            else:
                return float('inf')   
        elif isZero(mat):
            return 0
        else:      
            self.seen.add(hashed(mat))
            best = float('inf')
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    flip(mat, i, j)
                    best = min(best, 1 + self.inner(mat))
                    flip(mat, i, j)
            self.solutions[hashed(mat)] = best
            return best
        
    def minFlips(self, mat: List[List[int]]) -> int:
        ans = self.inner(mat)
        return ans if ans != float('inf') else -1
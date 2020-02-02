class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i, row in enumerate(mat):
            row.append(-i)
        mat.sort(key=lambda x: x.count(1))
        return [-row[-1] for row in mat[0:k]]

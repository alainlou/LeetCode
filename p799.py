class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0]*i for i in range(1, 101)]
        tower[0][0] = poured

        for i, r in enumerate(tower):
            if i == len(tower)-1:
                break
            for j, glass in enumerate(r):
                if glass >= 1:
                    tower[i+1][j] += (glass-1)/2
                    tower[i+1][j+1] += (glass-1)/2

        return min(1, tower[query_row][query_glass])

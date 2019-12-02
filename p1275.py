class Solution:
    def winner(self, grid):
        if (grid[0][0] != None and grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2])\
        or (grid[0][0] != None and grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0])\
        or (grid[0][0] != None and grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]):
            return grid[0][0]
        elif (grid[1][0] != None and grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2])\
        or (grid[0][1] != None and grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1])\
        or (grid[0][2] != None and grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]):
            return grid[1][1]
        elif (grid[2][0] != None and grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2])\
        or (grid[0][2] != None and grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2]):
            return grid[2][2]
        return None       
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[None]*3 for _ in range(3)]
        for i in range(len(moves)):
            if i%2 == 0:
                grid[moves[i][0]][moves[i][1]] = 'A'
            else:
                grid[moves[i][0]][moves[i][1]] = 'B'
        if self.winner(grid) != None:
            return self.winner(grid)
        return "Draw" if len(moves) == 9 else "Pending"
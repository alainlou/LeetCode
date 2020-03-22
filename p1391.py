class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        directions = {1: [1, 3], 2: [2, 4], 3: [3, 4], 4: [1, 4], 5: [2, 3], 6: [1, 2]}
        valid = {1: {1, 3, 5}, 2: {2, 3, 4}, 3: {1, 4, 6}, 4: {2, 5, 6}}

        q = [(0, 0)]

        def is_valid(i, j, d):
            if 0 <= i < m and 0 <= j < n and grid[i][j] in valid[d] and (i, j) not in visited:
                return True
            return False

        def helper(i, j, d):
            if d == 1 and is_valid(i, j+1, 1):
                q.append((i, j+1))
            elif d == 2 and is_valid(i-1, j, 2):
                q.append((i-1, j))
            elif d == 3 and is_valid(i, j-1, 3):
                q.append((i, j-1))
            elif d == 4 and is_valid(i+1, j, 4):
                q.append((i+1, j))

        while len(q) > 0:
            (i, j) = q.pop(0)
            visited.add((i, j))
            if i == m-1 and j == n-1:
                return True
            for d in directions[grid[i][j]]:
                helper(i, j, d)

        return False

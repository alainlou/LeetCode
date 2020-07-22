class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i, j, idx):
            if idx > len(word)-1:
                return True
            if board[i][j] == word[idx]:
                if idx == len(word)-1:
                    return True
                if i-1 >= 0 and (i-1, j) not in visited:
                    visited.add((i-1, j))
                    ret = dfs(i-1, j, idx+1)
                    if ret:
                        return True
                    visited.remove((i-1, j))
                if i+1 < len(board) and (i+1, j) not in visited:
                    visited.add((i+1, j))
                    ret = dfs(i+1, j, idx+1)
                    if ret:
                        return True
                    visited.remove((i+1, j))
                if j-1 >= 0 and (i, j-1) not in visited:
                    visited.add((i, j-1))
                    ret = dfs(i, j-1, idx+1)
                    if ret:
                        return True
                    visited.remove((i, j-1))
                if j+1 < len(board[0]) and (i, j+1) not in visited:
                    visited.add((i, j+1))
                    ret = dfs(i, j+1, idx+1)
                    if ret:
                        return True
                    visited.remove((i, j+1))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited.add((i, j))
                ret = dfs(i, j, 0)
                visited.remove((i, j))
                if ret:
                    return True

        return False

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        def small(one, two, three, four):
            if one is None and two is None:
                return 0 if three == 0 or four == 0 else None
            if one is None:
                return two
            if two is None:
                return one
            return min(one, two)

        def big(one, two, three, four):
            if one is None and two is None:
                return 0 if three == 0 or four == 0 else None
            if one is None:
                return two
            if two is None:
                return one
            return max(one, two)

        mod = 10**9+7
        m, n = len(grid), len(grid[0])

        dp_pos = [[None]*n for _ in range(m)]
        dp_neg = [[None]*n for _ in range(m)]

        dp_pos[0][0] = grid[0][0] if grid[0][0] >= 0 else None
        dp_neg[0][0] = grid[0][0] if grid[0][0] <= 0 else None

        for i in range(1, m):
            if grid[i][0] > 0:
                dp_pos[i][0] = dp_pos[i-1][0]*grid[i][0] if dp_pos[i-1][0] is not None else None
                dp_neg[i][0] = dp_neg[i-1][0]*grid[i][0] if dp_neg[i-1][0] is not None else None
            elif grid[i][0] < 0:
                dp_pos[i][0] = dp_neg[i-1][0]*grid[i][0] if dp_neg[i-1][0] is not None else None
                dp_neg[i][0] = dp_pos[i-1][0]*grid[i][0] if dp_pos[i-1][0] is not None else None
            else:
                dp_pos[i][0] = 0
                dp_neg[i][0] = 0

        for i in range(1, n):
            if grid[0][i] > 0:
                dp_pos[0][i] = dp_pos[0][i-1]*grid[0][i] if dp_pos[0][i-1] is not None else None
                dp_neg[0][i] = dp_neg[0][i-1]*grid[0][i] if dp_neg[0][i-1] is not None else None
            elif grid[0][i] < 0:
                dp_pos[0][i] = dp_neg[0][i-1]*grid[0][i] if dp_neg[0][i-1] is not None else None
                dp_neg[0][i] = dp_pos[0][i-1]*grid[0][i] if dp_pos[0][i-1] is not None else None
            else:
                dp_pos[0][i] = 0
                dp_neg[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    dp_pos[i][j] = big(dp_pos[i][j-1], dp_pos[i-1][j], dp_neg[i][j-1], dp_neg[i-1][j])*grid[i][j] if big(dp_pos[i][j-1], dp_pos[i-1][j], dp_neg[i][j-1], dp_neg[i-1][j]) is not None else None
                    dp_neg[i][j] = small(dp_neg[i][j-1], dp_neg[i-1][j], dp_pos[i][j-1], dp_pos[i-1][j])*grid[i][j] if small(dp_neg[i][j-1], dp_neg[i-1][j], dp_pos[i][j-1], dp_pos[i-1][j]) is not None else None
                elif grid[i][j] < 0:
                    dp_pos[i][j] = small(dp_neg[i][j-1], dp_neg[i-1][j], dp_pos[i][j-1], dp_pos[i-1][j])*grid[i][j] if small(dp_neg[i][j-1], dp_neg[i-1][j], dp_pos[i][j-1], dp_pos[i-1][j]) is not None else None
                    dp_neg[i][j] = big(dp_pos[i][j-1], dp_pos[i-1][j], dp_neg[i][j-1], dp_neg[i-1][j])*grid[i][j] if big(dp_pos[i][j-1], dp_pos[i-1][j], dp_neg[i][j-1], dp_neg[i-1][j]) is not None else None
                else:
                    dp_pos[i][j] = 0
                    dp_neg[i][j] = 0

        return dp_pos[-1][-1]%mod if dp_pos[-1][-1] is not None else -1

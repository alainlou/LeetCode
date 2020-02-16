from functools import lru_cache

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        bit_board = [0]*m
        for i in range(m):
            for j in range(n):
                bit_board[i] |= (1<<j) if seats[i][j] == '.' else 0

        def bit_count(n):
            ans = 0
            while n > 0:
                ans += 1
                n &= n-1
            return ans

        @lru_cache(maxsize = None)
        def recurse(prev_row, row_idx):
            if row_idx == m:
                return 0

            result = recurse(0, row_idx+1)
            state = bit_board[row_idx]

            while state > 0:
                if (state & (state << 1) == 0 and
                (prev_row << 1) & state == 0 and
                (state << 1) & prev_row == 0):
                        result = max(result, bit_count(state) + recurse(state, row_idx + 1))
                state = (state - 1) & bit_board[row_idx]

            return result

        return recurse(0, 0)

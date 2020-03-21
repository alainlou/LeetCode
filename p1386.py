class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        ans = 0
        curr_row = 0
        mask = 0

        for r in reservedSeats:
            if r[0] != curr_row:
                ans += 2*(r[0] - curr_row - 1)
                if mask & int('0111111110', 2) == int('0111111110', 2):
                    ans += 2
                elif mask & int('0111100000', 2) == int('0111100000', 2) \
                or mask & int('0000011110', 2) == int('0000011110', 2) \
                or mask & int('0001111000', 2) == int('0001111000', 2):
                    ans += 1
                mask = int('1111111111', 2) - (1 << (r[1]-1))
                curr_row = r[0]
            else:
                mask -= 1 << (r[1]-1)

        ans += 2*(n - curr_row)
        if mask & int('0111111110', 2) == int('0111111110', 2):
            ans += 2
        elif mask & int('0111100000', 2) == int('0111100000', 2) \
        or mask & int('0000011110', 2) == int('0000011110', 2) \
        or mask & int('0001111000', 2) == int('0001111000', 2):
            ans += 1

        return ans

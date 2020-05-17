class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        curr_len = 0
        curr = None

        for c in s:
            if c == curr:
                curr_len += 1
                ans = max(ans, curr_len)
            else:
                curr = c
                curr_len = 1

        return ans

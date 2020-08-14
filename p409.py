from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        ans = 0
        largest_odd = 1

        for v in counts.values():
            if v%2 == 0:
                ans += v
            elif v > largest_odd:
                ans += largest_odd - 1 if largest_odd > 0 else 0
                largest_odd = v
            else:
                ans += v-1

        return ans + largest_odd

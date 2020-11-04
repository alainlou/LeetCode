class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def is_one_diff(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = 0
            for i, c in enumerate(s1):
                if c != s2[i]:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        m, n = len(s), len(t)

        ans = 0

        for i in range(m):
            for j in range(i+1, m+1):
                for k in range(n):
                    if k+j-i <= n:
                        ans += is_one_diff(s[i:j], t[k:k+j-i])

        return ans

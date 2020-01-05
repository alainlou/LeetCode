class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        def recurse(s, start, end):
            if start == end:
                return 0
            if start+1 == end:
                return 0 if s[start] == s[end] else 1
            if (start, end) in memo:
                return memo[(start, end)]
            if s[start] == s[end]:
                ans = recurse(s, start+1, end-1)
                memo[(start, end)] = ans
                return ans
            else:
                ans = min(recurse(s, start, end-1), recurse(s, start+1, end)) + 1
                memo[(start, end)] = ans
                return ans
        return recurse(s, 0, len(s)-1)

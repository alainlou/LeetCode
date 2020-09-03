class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return len(s) > 0 and s in (s*2)[1:-1]

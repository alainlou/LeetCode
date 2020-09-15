class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split()
        return 0 if len(tmp) == 0 else len(tmp[-1])

class Solution:
    def reverseWords(self, s: str) -> str:
        return ''.join((sub+' ' if len(sub) > 0 else '') for sub in s.split(' ')[::-1]).strip()

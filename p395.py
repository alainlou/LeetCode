class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = [0]*26
        for c in s:
            counts[ord(c)-97] += 1
        for i in range(26):
            if 0 < counts[i] < k:
                return max([self.longestSubstring(substr, k) for substr in s.split(chr(i+97))])
        return len(s)

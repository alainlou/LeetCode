class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        i = 1
        while word*i in sequence:
            ans += 1
            i += 1
        return ans
                
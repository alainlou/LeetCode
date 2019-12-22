class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        def isValid(s, maxLetters):
            return len(set(s)) <= maxLetters
        
        n = len(s)
        ans = 0
        for l in range(minSize, maxSize+1):
            counts = {}
            for i in range(n-l+1):
                curr = s[i:i+l]
                if curr in counts:
                    counts[curr] += 1
                elif isValid(curr, maxLetters):
                    counts[curr] = 1
            ans = max(ans, max(counts.values())) if len(counts) > 0 else ans
        return ans
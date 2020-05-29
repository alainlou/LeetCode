from collections import defaultdict

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        vowels = ['a', 'e', 'i', 'o', 'u']
        ans = 0

        for i in range(k):
            counts[s[i]] += 1
            ans = sum(counts[c] for c in vowels)


        for i in range(k, len(s)):
            counts[s[i]] += 1
            counts[s[i-k]] -= 1
            ans = max(ans, sum(counts[c] for c in vowels))

        return ans

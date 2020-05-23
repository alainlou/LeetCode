from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        charset = [v*k for k, v in counts.items()]
        charset.sort(key=lambda x:-len(x))

        return ''.join(charset)

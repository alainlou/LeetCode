from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        h = 0
        for i in range(10):
            h *= 29
            h += ord(s[i])-ord('A')+1

        d = defaultdict(lambda: float('inf'))
        d[h] = 9
        seqs = set()

        for i in range(10, len(s)):
            h -= (ord(s[i-10])-ord('A')+1)*29**9
            h *= 29
            h += ord(s[i])-ord('A')+1
            if h in d:
                seqs.add(s[i-9:i+1])
            d[h] = min(d[h], i)

        return list(seqs)

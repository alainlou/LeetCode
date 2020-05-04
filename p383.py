from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = defaultdict(int)

        for c in magazine:
            counts[c] += 1

        for c in ransomNote:
            if counts[c] <= 0:
                return False
            counts[c] -= 1

        return True

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for w in words:
            add = True
            for c in w:
                if c not in allowed:
                    add = False
            if add:
                ans += 1
        return ans

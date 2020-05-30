class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        present = [False]*2**k
        bitmask = 0

        for i in range(k):
            bitmask *= 2
            bitmask += 1 if s[i] == '1' else 0

        present[bitmask] = True

        for i in range(k, len(s)):
            bitmask <<= 1
            bitmask += 1 if s[i] == '1' else 0
            bitmask %= 2**k
            present[bitmask] = True

        for p in present:
            if not p:
                return False

        return True

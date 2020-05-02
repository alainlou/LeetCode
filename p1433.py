from collections import defaultdict

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)

        for c in s1:
            counts1[c] += 1
        for c in s2:
            counts2[c] += 1

        # check s2 breaks s1
        success = True
        for c in s2:
            success = False
            idx = c
            while ord(idx) <= ord('z'):
                if counts1[idx] > 0:
                    counts1[idx] -= 1
                    success = True
                    break
                idx = chr(ord(idx)+1)
            if not success:
                break

        if success:
            return True

        # check s1 breaks s2:
        for c in s1:
            success = False
            idx = c
            while ord(idx) <= ord('z'):
                if counts2[idx] > 0:
                    counts2[idx] -= 1
                    success = True
                    break
                idx = chr(ord(idx)+1)
            if not success:
                break

        return success

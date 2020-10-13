from collections import Counter

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        mismatch = []

        for i, c in enumerate(A):
            if c != B[i]:
                mismatch.append(i)

        if len(mismatch) == 0:
            c = Counter(list(A))
            for v in c.values():
                if v > 1:
                    return True
            return False

        if len(mismatch) != 2:
            return False

        return A[mismatch[0]] == B[mismatch[1]] and A[mismatch[1]] == B[mismatch[0]]

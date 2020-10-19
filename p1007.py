class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        d = {'A': 0, 'B': 1}

        for i in range(1, len(A)):
            if A[0] not in (A[i], B[i]):
                d['A'] = float('inf')
            if B[0] not in (A[i], B[i]):
                d['B'] = float('inf')
            if min(d.values()) == float('inf'):
                return -1
            if A[i] != A[0] and B[i] == A[0]:
                d['A'] += 1
            if A[i] != B[0] and B[i] == B[0]:
                d['B'] += 1

        tmp1 = min(d.values())

        d = {'A': 1, 'B': 0}

        for i in range(1, len(A)):
            if A[0] not in (A[i], B[i]):
                d['A'] = float('inf')
            if B[0] not in (A[i], B[i]):
                d['B'] = float('inf')
            if min(d.values()) == float('inf'):
                return -1
            if B[i] != B[0] and A[i] == B[0]:
                d['B'] += 1
            if B[i] != A[0] and A[i] == A[0]:
                d['A'] += 1

        tmp2 = min(d.values())

        return min(tmp1, tmp2)

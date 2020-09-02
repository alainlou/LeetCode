from collections import defaultdict
from math import sqrt

from DS.DSU import DSU

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU(len(A))

        def prime_factorize(n):
            for i in range(2, int(sqrt(n))+1):
                if n%i == 0:
                    return [i] + prime_factorize(n//i)
            return [n]

        prime2indices = defaultdict(list)

        for i, n in enumerate(A):
            for p in prime_factorize(n):
                prime2indices[p].append(i)

        for arr in prime2indices.values():
            for i in range(1, len(arr)):
                dsu.union(arr[0], arr[i])

        aggregate = defaultdict(int)

        for i in range(len(A)):
            aggregate[dsu.find(i)] += 1

        return max(aggregate.values())

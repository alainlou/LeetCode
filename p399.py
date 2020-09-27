from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dct = defaultdict(lambda: defaultdict(int))

        for i, e in enumerate(equations):
            dct[e[0]][e[1]] = values[i]
            dct[e[1]][e[0]] = 1/values[i]

        for k0 in dct.keys():
            for k1 in dct.keys():
                for k2 in dct.keys():
                    if k1 in dct[k0].keys() and k2 in dct[k1].keys():
                        dct[k0][k2] = dct[k0][k1] * dct[k1][k2]
                        dct[k2][k0] = 1/(dct[k0][k1] * dct[k1][k2])

        ans = []

        for q in queries:
            if q[0] not in dct or q[1] not in dct[q[0]]:
                ans.append(-1)
            else:
                ans.append(dct[q[0]][q[1]])

        return ans

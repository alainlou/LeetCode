class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        find = list(range(n))
        groups = [set({i}) for i in range(n)]
        for c in connections:
            flag1 = find[c[0]]
            flag2 = find[c[1]]
            if flag1 != flag2:
                for i in groups[flag2]:
                    find[i] = flag1
                groups[flag1].update(groups[flag2])
        tmp = set()
        for i in find:
            tmp.add(i)
        return len(tmp)-1

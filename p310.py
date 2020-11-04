class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        d = defaultdict(set)

        for e in edges:
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])

        q = []
        next_q = []
        ans = defaultdict(list)
        max_dist = 0

        for k, e in d.items():
            if len(e) == 1:
                next_q.append((k, 0))

        while len(q) > 0 or len(next_q) > 0:
            if len(q) == 0:
                q += next_q
                next_q = []
            tmp = q.pop(0)
            curr, dist = tmp[0], tmp[1]
            max_dist = max(max_dist, dist)
            ans[dist].append(curr)
            for n in d[curr]:
                d[n].remove(curr)
                if len(d[n]) == 1:
                    next_q.append((n, dist+1))

        return ans[max_dist]

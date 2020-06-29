from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for t in tickets:
            adj[t[0]].append(t[1])

        for v in adj.values():
            v.sort()

        q = ['JFK']
        ans = []

        while len(q) > 0:
            curr = q[0]
            if len(adj[curr]) > 0:
                q.insert(0, adj[curr].pop(0))
            else:
                ans.insert(0, q.pop(0))

        return ans

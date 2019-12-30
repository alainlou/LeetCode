class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        children = {}
        n = len(arr)
        for i in range(n):
            children[i] = set()
            if i+arr[i] < n:
                children[i].add(i+arr[i])
            if i-arr[i] > -1:
                children[i].add(i-arr[i])
        q = [start]
        reachable = set()
        while len(q) > 0:
            curr = q.pop(0)
            reachable.add(curr)
            for c in children[curr]:
                if c not in reachable:
                    q.append(c)
        for node in reachable:
            if arr[node] == 0:
                return True
        return False

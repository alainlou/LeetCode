class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        jumps = {i:set() for i in arr}

        for i in range(n):
            jumps[arr[i]].add(i)

        visited = set()
        q = [(0, 0)]

        while len(q) > 0:
            curr = q.pop(0)
            idx = curr[0]
            depth = curr[1]
            visited.add(idx)

            if idx == n-1:
                return depth

            connected = set()
            if idx > 0 and idx-1:
                connected.add(idx-1)
            if idx < n-1 and idx+1:
                connected.add(idx+1)

            if arr[idx] in jumps:
                connected |= jumps[arr[idx]]
                del jumps[arr[idx]]

            for node in connected:
                if node not in visited:
                    visited.add(node)
                    q.append((node, depth + 1))

        return -1

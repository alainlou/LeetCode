class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cp = {}

        def dfs(node):
            if node is None:
                return None

            ret = Node(node.val, node.neighbors[:])
            cp[ret.val] = ret

            for i, n in enumerate(ret.neighbors):
                if n.val not in cp:
                    ret.neighbors[i] = dfs(n)
                    cp[ret.val] = ret
                ret.neighbors[i] = cp[n.val]

            return ret

        return dfs(node)

from collections import defaultdict

from DS.TreeNode import TreeNode

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = defaultdict(lambda: None)
        depth = defaultdict(lambda: int(-1))

        q = [(root, 0)]

        while len(q) > 0:
            curr = q.pop(0)
            node = curr[0]
            level = curr[1]
            depth[node.val] = level
            if node.left:
                parent[node.left.val] = node.val
                q.append((node.left, level + 1))
            if node.right:
                parent[node.right.val] = node.val
                q.append((node.right, level + 1))

        return depth[x] != -1 and depth[x] == depth[y] and parent[x] is not None and parent[x] != parent[y]

from functools import lru_cache
from DS.TreeNode import TreeNode

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        @lru_cache(None)
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def dfs(node):
            if node is None:
                return node
            left, right = height(node.left), height(node.right)
            if left == right:
                return node
            elif left > right:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(root)

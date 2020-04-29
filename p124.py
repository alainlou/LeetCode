from functools import lru_cache

from DS.TreeNode import TreeNode

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        @lru_cache(None)
        def from_root(node):
            if node is None:
                return 0
            return max(0, node.val + max(from_root(node.left), from_root(node.right)))

        @lru_cache(None)
        def dfs(node):
            if node is None:
                return float('-inf')
            return max(node.val + from_root(node.left) + from_root(node.right), dfs(node.left), dfs(node.right))

        return dfs(root)

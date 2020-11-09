
from functools import lru_cache

from DS.TreeNode import TreeNode

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        @lru_cache(None)
        def get_min(node):
            if node is None:
                return float('inf')
            return min(node.val, get_min(node.left), get_min(node.right))

        @lru_cache(None)
        def get_max(node):
            if node is None:
                return float('-inf')
            return max(node.val, get_max(node.left), get_max(node.right))

        def dfs(node):
            if node is None:
                return float('-inf')
            tmp = max(abs(node.val - get_max(node)), abs(node.val - get_min(node)))
            return max(tmp, dfs(node.left), dfs(node.right))

        return dfs(root)

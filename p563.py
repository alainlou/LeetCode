from functools import lru_cache

from DS.TreeNode import TreeNode

class Solution:
    def findTilt(self, root: TreeNode) -> int:

        @lru_cache(None)
        def sum_under(node):
            if node is None:
                return 0
            return node.val + sum_under(node.left) + sum_under(node.right)

        def tilt(node):
            if node is None:
                return 0
            return abs(sum_under(node.right) - sum_under(node.left))


        def dfs(node):
            if node is None:
                return 0
            return dfs(node.left) + tilt(node) + dfs(node.right)

        return dfs(root)

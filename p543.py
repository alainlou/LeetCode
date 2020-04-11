from functools import lru_cache

from DS.TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        @lru_cache(None)
        def height(node):
            if node is None:
                return -1
            return 1 + max(height(node.left), height(node.right))

        def dfs(node):
            if node is None:
                return -1
            return max(2 + height(node.left) + height(node.right), \
                       dfs(node.left), dfs(node.right))

        return dfs(root)

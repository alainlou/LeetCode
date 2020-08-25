from DS.TreeNode import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0

        def dfs(node, value):
            if node is None:
                return 0
            value += node.val
            if value == sum:
                return 1 + dfs(node.left, value) + dfs(node.right, value)
            return dfs(node.left, value) + dfs(node.right, value)

        return dfs(root, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

from DS.TreeNode import TreeNode

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.ans = 0

        def dfs(node, tmp):
            tmp *= 2
            tmp += node.val
            if node.left is None and node.right is None:
                self.ans += tmp
            if node.left is not None:
                dfs(node.left, tmp)
            if node.right is not None:
                dfs(node.right, tmp)

        dfs(root, 0)
        return self.ans

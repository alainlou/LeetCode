from DS.TreeNode import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None or (root.left is None and root.right is None):
            return root

        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp

        return root

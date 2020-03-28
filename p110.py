from DS.TreeNode import TreeNode

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height(root):
            if root is None:
                return 0
            l = height(root.left)
            r = height(root.right)
            if l == -1 or r == -1:
                return -1
            return 1 + max(l, r) if abs(l - r) <= 1 else -1

        return height(root) >= 0

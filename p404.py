from DS.TreeNode import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def recurse(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0
            return recurse(node.left, True) + recurse(node.right, False)

        return recurse(root, False)

from DS.TreeNode import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(root, lo=float('-inf'), hi=float('inf')):
            if root is None:
                return True
            if root.val <= lo or root.val >= hi:
                return False
            return validate(root.left, lo, root.val) and validate(root.right, root.val, hi)

        return validate(root)

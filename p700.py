from DS.TreeNode import TreeNode

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root

        if val > root.val:
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)

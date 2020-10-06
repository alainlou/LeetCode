from DS.TreeNode import TreeNode

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root

        while curr:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    return root
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    return root

        return TreeNode(val)

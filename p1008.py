from DS.TreeNode import TreeNode

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        ret = TreeNode(preorder.pop(0))

        idx = 0

        while idx < len(preorder) and preorder[idx] < ret.val:
            idx += 1

        ret.left = self.bstFromPreorder(preorder[:idx])
        ret.right = self.bstFromPreorder(preorder[idx:])

        return ret

from DS.TreeNode import TreeNode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        n = inorder.index(root.val)
        root.left = self.buildTree(inorder[:n], postorder[:n])
        root.right = self.buildTree(inorder[n+1:], postorder[n:-1])
        return root

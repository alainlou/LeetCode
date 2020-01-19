from DS.TreeNode import TreeNode

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def process(root, target):
            if root is None:
                return False
            if process(root.left, target):
                root.left = None
            if process(root.right, target):
                root.right = None
            if root.left is None and root.right is None and root.val == target:
                return True
            return False

        if process(root, target):
            return None
        return root

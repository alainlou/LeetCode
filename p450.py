from DS.TreeNode import TreeNode

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        def predecessor(root):
            if not root:
                return None
            if root.right and not root.right.right:
                tmp = root.right
                root.right = root.right.left
                tmp.left = None
                return tmp
            if root.right:
                return predecessor(root.right)
            return root

        def successor(root):
            if not root:
                return None
            if root.left and not root.left.left:
                tmp = root.left
                root.left = root.left.right
                tmp.right = None
                return tmp
            if root.left:
                return successor(root.left)
            return root

        if root.val == key:
            tmp = successor(root.right)
            if tmp:
                tmp.left = root.left
                if tmp != root.right:
                    tmp.right = root.right
                return tmp
            tmp = predecessor(root.left)
            if tmp:
                tmp.right = root.right
                if tmp != root.left:
                    tmp.left = root.left
                return tmp
            return tmp

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

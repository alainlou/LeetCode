from DS.TreeNode import TreeNode

class Solution:
    def __init__(self):
        self.ans = None

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.ans = float('inf')

        def dfs(node, level):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.ans = min(self.ans, level)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 1)

        return self.ans

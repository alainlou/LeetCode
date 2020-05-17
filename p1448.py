from DS.TreeNode import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, maximum):
            if node.val >= maximum:
                self.ans += 1
            if node.left:
                dfs(node.left, max(maximum, node.val))
            if node.right:
                dfs(node.right, max(maximum, node.val))

        dfs(root, float('-inf'))

        return self.ans

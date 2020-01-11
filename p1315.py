from DS.TreeNode import TreeNode

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def helper(root, level):
            if level == 0 and root:
                return root.val
            if root is None:
                return 0
            return helper(root.left, level-1) + helper(root.right, level-1)

        def dfs(root):
            ans = 0
            if root is None:
                return 0
            if root.val%2 == 0:
                ans += helper(root, 2)
            ans += dfs(root.left) + dfs(root.right)
            return ans

        return dfs(root)

from DS.TreeNode import TreeNode

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        ans = 0
        def recurse(node, i):
            if node is None:
                return 0
            curr = node.val
            if node.left is not None:
                curr += recurse(node.left, i*2+1)
            if node.right is not None:
                curr += recurse(node.right, i*2+2)
            return curr
        root_sum = recurse(root, 0)
        def solve(node, i):
            nonlocal ans
            if node is None:
                return 0
            curr = node.val
            if node.left is not None:
                curr += solve(node.left, i*2+1)
            if node.right is not None:
                curr += solve(node.right, i*2+2)
            ans = max(ans, (root_sum-curr)*curr)
            return curr
        solve(root, 0)
        return ans%(10**9+7)

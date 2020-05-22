from DS.TreeNode import TreeNode

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k

        def dfs(node):
            if node.left is not None:
                ret = dfs(node.left)
                if ret is not None:
                    return ret
            self.k -= 1
            if self.k == 0:
                return node.val
            if node.right is not None:
                ret = dfs(node.right)
                if ret is not None:
                    return ret

        return dfs(root)

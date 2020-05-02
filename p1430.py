from DS.TreeNode import TreeNode

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:

        def dfs(node, idx):
            if node is None:
                return False
            if idx == len(arr) - 1:
                return arr[idx] == node.val and node.left is None and node.right is None
            return arr[idx] == node.val and (dfs(node.left, idx + 1) or dfs(node.right, idx + 1))

        return dfs(root, 0)

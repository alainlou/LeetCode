from DS.TreeNode import TreeNode

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            arr.append(node)
            dfs(node.right)

        dfs(root)

        arr[-1].left = None
        arr[-1].right = None
        for i in range(len(arr)-2, -1, -1):
            arr[i].left = None
            arr[i].right = arr[i+1]

        return arr[0]

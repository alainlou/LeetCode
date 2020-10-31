from DS import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        arr = []
        def dfs(node):
            if node.left is None and node.right is None:
                arr.append(node)
                return
            if node.left:
                dfs(node.left)
            arr.append(node)
            if node.right:
                dfs(node.right)
            return

        dfs(root)

        n = len(arr)

        for i in range(n-1, -1, -1):
            if arr[i].val < arr[i-1].val:
                for j in range(i-1, -1, -1):
                    if arr[j].val > arr[i].val:
                        arr[i].val, arr[j].val = arr[j].val, arr[i].val

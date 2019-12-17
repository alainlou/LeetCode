from DS.TreeNode import TreeNode

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:  
        self.bucket = 0
        def solve(node):
            if node == None:
                return
            solve(node.right)
            node.val += self.bucket
            self.bucket = node.val
            solve(node.left)
        solve(root)
        return root
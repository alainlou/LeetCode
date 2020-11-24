from functools import lru_cache
from DS.TreeNode import TreeNode

class Solution:
    def rob(self, root: TreeNode) -> int:
        
        @lru_cache(None)
        def dfs(node):
            if node is None:
                return 0
            
            ans = node.val
            if node.left:
                ans += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                ans += dfs(node.right.left) + dfs(node.right.right)
                
            return max(ans, dfs(node.left) + dfs(node.right))
        
        return dfs(root)
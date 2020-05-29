from DS.TreeNode import TreeNode

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.ans = 0

        def check_path(counts):
            if sum(counts)%2 == 0:
                for c in counts:
                    if c%2 != 0:
                        return False
                return True
            else:
                flag = False
                for c in counts:
                    if c%2 == 1 and not flag:
                        flag = True
                    elif c%2 == 1:
                        return False
                return flag

        def dfs(node, counts):
            counts[node.val-1] += 1
            if node.left is None and node.right is None:
                if check_path(counts):
                    self.ans += 1
            if node.left:
                dfs(node.left, counts)
            if node.right:
                dfs(node.right, counts)
            counts[node.val-1] -= 1

        dfs(root, [0]*9)

        return self.ans

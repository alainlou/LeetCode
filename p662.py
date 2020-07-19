from DS.TreeNode import TreeNode

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        ans = 0
        level = 0
        left, right = float('inf'), float('-inf')

        q = [(root, 0, 0)]

        while len(q) > 0:
            curr = q.pop(0)
            if curr[2] > level:
                ans = max(ans, right - left + 1)
                left, right = float('inf'), float('-inf')
                level = curr[2]
            left = min(left, curr[1])
            right = max(right, curr[1])
            if curr[0].left:
                q.append((curr[0].left, 2*curr[1], curr[2]+1))
            if curr[0].right:
                q.append((curr[0].right, 2*curr[1]+1, curr[2]+1))

        ans = max(ans, right - left + 1)

        return ans

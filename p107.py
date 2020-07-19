from DS.TreeNode import TreeNode

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        q = [(root, 0)]
        ans = []
        level = []
        curr_level = 0

        while len(q) > 0:
            curr = q.pop(0)
            if curr[0].left:
                q.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                q.append((curr[0].right, curr[1]+1))
            if curr[1] > curr_level:
                ans.insert(0, level)
                level = []
                curr_level = curr[1]
            level.append(curr[0].val)

        if len(level) > 0:
            ans.insert(0, level)

        return ans

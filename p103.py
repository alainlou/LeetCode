from DS.TreeNode import TreeNode

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = [(root, 0)]
        while len(q) > 0:
            curr = q.pop(0)
            if len(ans) <= curr[1]:
                ans.append([])
            ans[-1].append(curr[0].val)
            if curr[0].left:
                q.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                q.append((curr[0].right, curr[1]+1))
        for i in range(1, len(ans), 2):
            ans[i] = ans[i][::-1]
        return ans

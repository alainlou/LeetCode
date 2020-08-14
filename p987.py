from collections import defaultdict

from DS.TreeNode import TreeNode

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        loc = defaultdict(lambda: defaultdict(list))

        q = [(root, 0, 0)]

        while len(q) > 0:
            curr = q.pop(0)
            loc[curr[1]][curr[2]].append(curr[0].val)
            if curr[0].left:
                q.append((curr[0].left, curr[1]-1, curr[2]+1))
            if curr[0].right:
                q.append((curr[0].right, curr[1]+1, curr[2]+1))

        ans = []

        for k0 in sorted(loc.keys()):
            col = []
            for k1 in sorted(loc[k0].keys()):
                col += sorted(loc[k0][k1])
            ans.append(col)

        return ans

from collections import defaultdict
from DS.TreeNode import TreeNode

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        d = defaultdict(list)

        q = [(root, 0)]

        while len(q) > 0:
            curr = q.pop(0)
            if curr[1]%2 == 0:
                if curr[0].val%2 == 0 or (len(d[curr[1]]) > 0 and d[curr[1]][-1] >= curr[0].val):
                    return False
            else:
                if curr[0].val%2 == 1 or (len(d[curr[1]]) > 0 and d[curr[1]][-1] <= curr[0].val):
                    return False
            d[curr[1]].append(curr[0].val)
            if curr[0].left:
                q.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                q.append((curr[0].right, curr[1]+1))

        return True

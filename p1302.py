from DS.TreeNode import TreeNode

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = 0
        arr = []
        q = [[root, 0]]
        while len(q) > 0:
            curr = q.pop(0)
            if curr[1] > depth:
                depth = curr[1]
                arr = [curr[0].val]
            else:
                arr.append(curr[0].val)
            if curr[0].left:
                q.append([curr[0].left, curr[1]+1])
            if curr[0].right:
                q.append([curr[0].right, curr[1]+1])
        return sum(arr)

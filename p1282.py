class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        ans = []
        for i in range(len(groupSizes)):
            g = groupSizes[i]
            if g not in groups:
                groups[g] = [[i]]
            elif len(groups[g][-1]) < g:
                groups[g][-1].append(i)
            else:
                groups[g].append([i])
        for g in groups.values():
            for a in g:
                ans.append(a)
        return ans
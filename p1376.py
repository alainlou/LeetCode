from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        children = defaultdict(list)
        for i, m in enumerate(manager):
            children[m].append(i)

        ans = 0

        q = [(headID, 0)]

        while len(q) > 0:
            curr = q.pop(0)
            ans = max(ans, curr[1])
            for child in children[curr[0]]:
                q.append((child, informTime[curr[0]]+curr[1]))

        return ans

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        children = defaultdict(list)
        parents = defaultdict(set)

        for a, b in prerequisites:
            children[b].append(a)
            parents[a].add(b)

        q = []
        ans = []

        for i in range(numCourses):
            if len(parents[i]) == 0:
                q.append(i)

        while len(q) > 0:
            curr = q.pop(0)
            ans.append(curr)

            for c in children[curr]:
                parents[c].remove(curr)
                if len(parents[c]) == 0:
                    q.append(c)

        return ans if len(ans) == numCourses else []

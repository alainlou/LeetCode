class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parents = {}
        children = {}
        for p in prerequisites:
            if p[0] not in parents:
                parents[p[0]] = set({p[1]})
            else:
                parents[p[0]].add(p[1])
            if p[1] not in children:
                children[p[1]] = set({p[0]})
            else:
                children[p[1]].add(p[0])
        q = []
        for i in range(numCourses):
            if i not in parents:
                q.append(i)
        while len(q) > 0:
            curr = q.pop(0)
            if curr in children:
                for c in children[curr]:
                    parents[c].remove(curr)
                    if len(parents[c]) == 0:
                        q.append(c)
                        del parents[c]
        return len(parents) == 0

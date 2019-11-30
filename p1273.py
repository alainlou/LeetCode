class Solution:
    def compute(self, node, children, value):
        if node not in children:
            return value[node]
        for child in children[node]:
            value[node] += self.compute(child, children, value)
        return value[node]
    
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        exists = [True] * nodes
        ans = nodes
        children = {}
        for i in range(len(parent)):
            if parent[i] == -1:
                continue
            if parent[i] not in children:
                children[parent[i]] = []
            children[parent[i]].append(i)        
        
        self.compute(0, children, value)
        
        for i in range(len(value)):
            if value[i] == 0 and exists[i]:
                # delete the subtree
                q = [i]
                while len(q) > 0:
                    node = q.pop(0)
                    exists[node] = False
                    if node in children:
                        for child in children[node]:
                            if exists[child]:
                                q.append(child)
        ans = 0
        for e in exists:
            if e == True:
                ans += 1
        return ans
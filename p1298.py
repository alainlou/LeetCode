class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        q = []
        haveKey = {}
        boxes = {}
        visited = {}
        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
            else:
                boxes[box] = True
        while len(q) != 0:
            curr = q.pop(0)
            ans += candies[curr]
            for k in keys[curr]:
                haveKey[k] = True
                if k not in visited and k in boxes:
                    q.append(k)
                    visited[k] = True
            for b in containedBoxes[curr]:
                boxes[b] = True
                if b not in visited and (b in haveKey or status[b] == 1):
                    q.append(b)
                    visited[b] = True
        return ans
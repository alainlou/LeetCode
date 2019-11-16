class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = {}
        for lst in regions:
            parent = lst[0]
            for i in range(1, len(lst)):
                parents[lst[i]] = parent
        family1 = []
        curr = region1
        while True:
            family1.append(curr)
            if curr not in parents.keys():
                break
            curr = parents[curr]
        family2 = []
        curr = region2
        while True:
            family2.append(curr)
            if curr not in parents.keys():
                break
            curr = parents[curr]
        for region in family1:
            if region in family2:
                return region
from collections import defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        furthest = defaultdict(int)

        for i, c in enumerate(S):
            furthest[c] = i

        start = 0
        ans = []

        while start < n:
            end = furthest[S[start]]
            idx = start
            while idx < end:
                end = max(end, furthest[S[idx]])
                idx += 1
            ans.append(end-start+1)
            start = end+1

        return ans

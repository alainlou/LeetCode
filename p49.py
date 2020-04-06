from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        ans = []

        for s in strs:
            counts = [0]*26

            for c in s:
                counts[ord(c)-ord('a')] += 1

            d[str(counts)].append(s)

        for val in d.values():
            ans.append(val)

        return ans

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts = [0]*26
        window = [0]*26
        ans = []

        for c in p:
            counts[ord(c)-ord('a')] += 1

        for i, c in enumerate(s):
            window[ord(c)-ord('a')] += 1
            if i >= len(p):
                window[ord(s[i-len(p)])-ord('a')] -= 1
            if i >= len(p)-1:
                for j in range(26):
                    if counts[j] != window[j]:
                        break
                else:
                    ans.append(i+1-len(p))

        return ans

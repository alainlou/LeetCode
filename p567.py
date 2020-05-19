class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = [0]*26
        window = [0]*26

        for c in s1:
            counts[ord(c)-ord('a')] += 1

        for i, c in enumerate(s2):
            window[ord(c)-ord('a')] += 1
            if i >= len(s1):
                window[ord(s2[i-len(s1)])-ord('a')] -= 1
            if i >= len(s1)-1:
                for j in range(26):
                    if counts[j] != window[j]:
                        break
                else:
                    return True

        return False

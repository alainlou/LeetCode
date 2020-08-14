class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if ord('a') <= ord(word[0]) <= ord('z'):
            for c in word:
                if ord('A') <= ord(c) <= ord('Z'):
                    return False
            return True

        cap = len(word) > 1 and ord('A') <= ord(word[1]) <= ord('Z')
        for i in range(2, len(word)):
            if (cap and not ord('A') <= ord(word[i]) <= ord('Z')) or (not cap and not ord('a') <= ord(word[i]) <= ord('z')):
                return False

        return True

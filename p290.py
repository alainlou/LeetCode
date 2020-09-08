class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lst = str.split()

        if len(lst) != len(pattern):
            return False

        dct = {}

        for i, c in enumerate(pattern):
            if c not in dct:
                if lst[i] in dct.values():
                    return False
                dct[c] = lst[i]
            else:
                if lst[i] != dct[c]:
                    return False

        return True

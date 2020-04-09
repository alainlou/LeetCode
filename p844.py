class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = list(S)
        t = list(T)

        idx = 0

        while idx < len(s):
            if s[idx] == '#' and idx == 0:
                del s[idx]
            elif s[idx] == '#':
                del s[idx-1]
                del s[idx-1]
                idx -= 1
            else:
                idx += 1

        idx = 0

        while idx < len(t):
            if t[idx] == '#' and idx == 0:
                del t[idx]
            elif t[idx] == '#':
                del t[idx-1]
                del t[idx-1]
                idx -= 1
            else:
                idx += 1

        return "".join(s) == "".join(t)

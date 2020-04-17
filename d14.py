class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final = 0

        for step in shift:
            final += (1 if step[0] == 0 else -1) * step[1]

        final %= len(s)

        return s[final:] + s[:final]

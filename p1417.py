class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        numeric = []

        for c in s:
            if ord('a') <= ord(c) <= ord('z'):
                alpha.append(c)
            else:
                numeric.append(c)

        if abs(len(alpha) - len(numeric)) > 1:
            return ""

        first = alpha if len(alpha) > len(numeric) else numeric
        second = numeric if len(alpha) > len(numeric) else alpha

        for i in range(len(second)):
            first.insert(2*i+1, second[i])

        return ''.join(first)

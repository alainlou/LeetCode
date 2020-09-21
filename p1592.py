class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = text.count(' ')
        c = s
        t = text.split()

        ans = []

        for i, w in enumerate(t):
            ans.append(w)
            if i < len(t)-1:
                ans.append(' '*(s//(len(t)-1)))
                c -= s//(len(t)-1)

        ans.append(' '*c)

        return ''.join(ans)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = {c: i for i, c in enumerate(s)}
        ans = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            while len(ans) > 0 and last_idx[ans[-1]] > i and ord(ans[-1]) > ord(c):
                seen.remove(ans.pop())
            ans.append(c)
            seen.add(c)

        return ''.join(ans)

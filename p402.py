class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        n = len(num)

        for n in num:
            while k > 0 and len(s) > 0 and s[-1] > n:
                del s[-1]
                k -= 1
            s.append(n)

        while k > 0:
            del s[-1]
            k -= 1

        ans = ''.join(s).lstrip('0')
        return ans if len(ans) > 0 else '0'

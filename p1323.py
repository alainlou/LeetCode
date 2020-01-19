class Solution:
    def maximum69Number(self, num: int) -> int:
        n = list(str(num))
        for i, dig in enumerate(n):
            if dig == '6':
                n[i] = '9'
                break
        return int("".join(n))

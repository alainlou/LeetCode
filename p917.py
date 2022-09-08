class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst = list(s)
        n = len(s)
        pntr1 = 0
        pntr2 = n - 1

        while True:
            while pntr1 < n and not lst[pntr1].isalpha():
                pntr1 += 1
            while pntr2 >= 0 and not lst[pntr2].isalpha():
                pntr2 -= 1
            if pntr1 >= pntr2:
                break
            lst[pntr1], lst[pntr2] = lst[pntr2], lst[pntr1]
            pntr1 += 1
            pntr2 -= 1

        return ''.join(lst)

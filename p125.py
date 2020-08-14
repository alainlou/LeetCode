class Solution:
    def isPalindrome(self, s: str) -> bool:

        def f(c):
            return ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

        lst = list(filter(f, list(s.lower())))

        for i in range(len(lst)//2):
            if lst[i] != lst[~i]:
                return False

        return True

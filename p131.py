class Solution:
    def isPalindrome(self, s, left, right):
        for i in range((right-left+1)//2):
            if s[left+i] != s[right-i]:
                return False
        return True
    def process(self, s, curr, left, right, ans):
        if right == len(s)-1:
            ans.append(curr)
            return
        nleft = right+1
        nright = nleft
        while nright < len(s):
            if self.isPalindrome(s, nleft, nright):
                self.process(s, curr+[s[nleft:nright+1]], nleft, nright, ans)
            nright += 1
    def partition(self, s: str) -> List[List[str]]:
        left = 0
        right = 0
        ans = []
        while right < len(s):
            if self.isPalindrome(s, left, right):
                self.process(s, [s[left:right+1]], left, right, ans)
            right += 1
        return ans
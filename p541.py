class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        l = []
        
        for i in range(0, n, 2*k):
            first = s[i:i+k]
            second = s[i+k:i+2*k]
            l.append(first[::-1])
            l.append(second)
            
        return ''.join(l)       

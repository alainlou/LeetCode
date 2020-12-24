class Solution:
    def nextGreaterElement(self, n: int) -> int:
        l = list(str(n))
        hi = '/'
        target = None
        
        for i in range(len(l)-1, -1, -1):
            if l[i] < hi:
                for j in range(len(l)-1, i, -1):
                    if l[j] > l[i] and l[j] < l[target]:
                        target = j
                l[i], l[target] = l[target], l[i]
                l[i+1::] = sorted(l[i+1::])
                tmp = int(''.join(l))
                return tmp if tmp < 2**31 else -1
            if l[i] > hi:
                hi = l[i]
                target = i
        
        return -1

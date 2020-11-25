class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        seen = set()
        
        tmp = 0
        i = 1
        
        while True:
            tmp *= 10
            tmp += 1
            tmp %= K
            if tmp == 0:
                return i
            elif tmp in seen:
                return -1
            seen.add(tmp)
            i += 1
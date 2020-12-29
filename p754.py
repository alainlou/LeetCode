class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        
        curr = 0
        i = 0
        
        while curr < target:
            i += 1
            curr += i
            
        if curr == target or (curr-target)%2 == 0:
            return i
        
        if (curr+i+1-target)%2 == 0:
            return i+1
        
        return i+2

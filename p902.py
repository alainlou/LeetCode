from bisect import bisect_left

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        num = [c for c in str(n)]
        num_len = len(num)
        
        ans = 1
        
        for c in num:
            if c not in digits:
                ans -= 1
                break
        
        for i in range(num_len-1, 0, -1):
            ans += len(digits)**i
    
        for i in range(num_len-1, -1, -1):
            dont_add = False
            for j in range(i):
                if num[j] not in digits:
                    dont_add = True
                    break
            if dont_add:
                continue
            ans += bisect_left(digits, num[i]) * len(digits)**(num_len-1-i)
            
        return ans
            
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                s.remove(n)
        
        return list(s)
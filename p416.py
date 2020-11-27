class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        possible = set()
        n = len(nums)
        s = sum(nums)
    
        if s%2 != 0:
            return False
        
        for i, n in enumerate(nums):
            to_add = {n}
            for p in possible:
                to_add.add(n+p)
            possible.update(to_add)
        
        return s//2 in possible
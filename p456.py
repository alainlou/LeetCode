class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        cand = []
        lo, hi = float('inf'), float('-inf')

        for n in nums:
            if lo < n < hi:
                return True
            for c in cand:
                if c[0] < n < c[1]:
                    return True
            if n > hi:
                hi = n
            if n < lo:
                cand.append((lo, hi))
                lo = n
                hi = lo

        return False

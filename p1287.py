class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        curr = None
        streak = 0
        for num in arr:
            if num == curr:
                streak += 1
                if streak > n//4:
                    return curr
            else:
                curr = num
                streak = 1
        return curr
        
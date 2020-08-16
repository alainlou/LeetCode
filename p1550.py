class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        for i, e in enumerate(arr):
            if e%2 == 1 and i < len(arr)-2 and arr[i+1]%2 == 1 and arr[i+2]%2 == 1:
                return True

        return False

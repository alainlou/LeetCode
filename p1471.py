class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        med = arr[((n - 1) // 2)]
        arr.sort(key=lambda x: abs(x-med))
        return arr[-k:]

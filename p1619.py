class Solution:
    def trimMean(self, arr: List[int]) -> float:
        p5 = len(arr)//20
        arr.sort()
        s = sum(arr) - sum(arr[:p5]) - sum(arr[-p5:])
        return s/(len(arr)-2*p5)

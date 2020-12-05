class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        for i, f in enumerate(flowerbed):
            if not f and (i == 0 or not flowerbed[i-1]) and (i == l-1 or not flowerbed[i+1]):
                n -= 1
                flowerbed[i] = 1
        return n <= 0

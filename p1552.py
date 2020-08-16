class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def check(distance):
            count = m-1
            last = position[0]

            for i in range(1, len(position)):
                if position[i]-last >= distance:
                    count -= 1
                    last = position[i]

            return count <= 0

        left, right = 0, position[-1]-position[0]+1

        while left < right-1:
            mid = (left+right)//2
            if check(mid):
                left = mid
            else:
                right = mid

        return left

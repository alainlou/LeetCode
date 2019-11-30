# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        ans = 0
        if not sea.hasShips(topRight, bottomLeft):
            return ans
        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return 1 if sea.hasShips(topRight, bottomLeft) else 0
        elif topRight.x - bottomLeft.x > 0:
            mid = (topRight.x+bottomLeft.x)//2
            nBL = Point(mid+1, bottomLeft.y)
            ans += self.countShips(sea, topRight, nBL)
            nTR = Point(mid, topRight.y)
            ans += self.countShips(sea, nTR, bottomLeft)
        else:
            mid = (topRight.y+bottomLeft.y)//2
            nBL = Point(bottomLeft.x, mid+1)
            ans += self.countShips(sea, topRight, nBL)
            nTR = Point(topRight.x, mid)
            ans += self.countShips(sea, nTR, bottomLeft)
        return ans
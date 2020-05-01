# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        left, right = 0, n

        while left != right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1

        return left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def insert(lst, e):
            if len(lst) == 0:
                lst.append(e)
                return 0
            if len(lst) == 1:
                if e > lst[0]:
                    lst.append(e)
                    return 1
                lst.insert(0, e)
                return 0

            left, right = 0, len(lst)
            mid = (left+right)//2

            while left < right-1:
                if e <= lst[mid]:
                    right = mid
                elif e > lst[mid]:
                    left = mid
                mid = (left+right)//2

            if lst[mid] < e:
                mid += 1

            lst.insert(mid, e)
            return mid

        ans, lst = [], []

        for n in nums[::-1]:
            ans.insert(0, insert(lst, n))

        return ans

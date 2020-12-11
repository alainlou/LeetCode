class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        n = len(arr)

        if n < 3:
            return False

        i = 0

        while i < n-1:
            if arr[i+1] > arr[i]:
                i += 1
            else:
                break


        j = n-1

        while j > 0:
            if arr[j-1] > arr[j]:
                j -= 1
            else:
                break

        return i == j and 0 < i < n-1

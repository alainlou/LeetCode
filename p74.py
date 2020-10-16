class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(arr, n):
            if len(arr) == 0:
                return False

            left, right = 0, len(arr)
            mid = (left+right)//2

            while left < mid:
                if arr[mid] > n:
                    right = mid
                else:
                    left = mid
                mid = (left+right)//2

            return arr[left] == n

        left, right = 0, len(matrix)
        mid = (left+right)//2

        while left < mid:
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return bin_search(matrix[mid], target)
            elif matrix[mid][0] > target:
                right = mid
            else:
                left = mid+1
            mid = (left+right)//2

        return 0 <= mid < len(matrix) and bin_search(matrix[mid], target)

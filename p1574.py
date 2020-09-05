class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        left_end, right_end = 0, len(arr)-1

        while left_end < len(arr)-1:
            if left_end+1 < len(arr) and arr[left_end+1] < arr[left_end]:
                break
            left_end += 1

        while right_end > 0:
            if right_end-1 > -1 and arr[right_end-1] > arr[right_end]:
                break
            right_end -= 1

        merge = float('-inf')

        left, right = 0, max(right_end, left_end+1)

        while left <= left_end and right < len(arr):
            if arr[left] > arr[right]:
                right += 1
            else:
                merge = max(merge, left + 1 + len(arr) - right)
                left += 1

        return len(arr) - max(left_end+1, len(arr)-right_end, merge)

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        def insert(A, n):
            if len(A) == 0 or n >= A[-1]:
                A.append(n)
                if len(A) > 1 and A[-1] - A[-2] <= t:
                    return True
            else:
                left, right = 0, len(A)
                mid = (left+right)//2

                while left < right-1:
                    if A[mid] <= n:
                        left = mid
                    else:
                        right = mid
                    mid = (left+right)//2

                if A[mid] < n:
                    mid += 1

                A.insert(mid, n)

                if 0 <= mid-1 and A[mid] - A[mid-1] <= t:
                    return True
                if mid+1 < len(A) and A[mid+1] - A[mid] <= t:
                    return True
                return False

        def delete(A, n):
            left, right = 0, len(A)
            mid = (left+right)//2

            while left < right-1:
                if A[mid] <= n:
                    left = mid
                else:
                    right = mid
                mid = (left+right)//2

            del A[mid]

        buffer = []

        for i in range(min(len(nums), k+1)):
            if insert(buffer, nums[i]):
                return True

        for i in range(k+1, len(nums)):
            delete(buffer, nums[i-k-1])
            if insert(buffer, nums[i]):
                return True

        return False

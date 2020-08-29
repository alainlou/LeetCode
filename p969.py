class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        right = len(A)-1
        ans = []

        while right > 0:
            largest = A[0]
            idx = 0
            for i in range(1, right+1):
                if A[i] > largest:
                    largest = A[i]
                    idx = i
            if idx == right:
                right -= 1
                continue
            A[:idx+1] = A[idx::-1]
            ans.append(idx+1)
            A[:right+1] = A[right::-1]
            ans.append(right+1)
            right -= 1

        return ans

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        def findMax(A):
            ans = ''
            max_hour = float('-inf')
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    tmp0 = 10*int(A[i])+int(A[j])
                    tmp1 = 10*int(A[j])+int(A[i])
                    if tmp0 < 24 and tmp0 > max_hour:
                        minute = findMaxMinute([A[x] for x in [0, 1, 2, 3] if x not in (i, j)])
                        if minute != float('-inf'):
                            ans = str(tmp0).zfill(2) + ':' + str(minute).zfill(2)
                            max_hour = tmp0
                    if tmp1 < 24 and tmp1 > max_hour:
                        minute = findMaxMinute([A[x] for x in [0, 1, 2, 3] if x not in (i, j)])
                        if minute != float('-inf'):
                            ans = str(tmp1).zfill(2) + ':' + str(minute).zfill(2)
                            max_hour = tmp1
            return ans

        def findMaxMinute(A):
            ans = float('-inf')
            tmp0 = 10*int(A[0])+int(A[1])
            tmp1 = 10*int(A[1])+int(A[0])
            if ans < tmp0 < 60:
                ans = tmp0
            if ans < tmp1 < 60:
                ans = tmp1
            return ans

        return findMax(A)

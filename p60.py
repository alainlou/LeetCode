class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        @lru_cache(None)
        def fact(n):
            if n == 1 or n == 0:
                return 1
            return n * fact(n-1)

        arr = [str(i+1) for i in range(n)]

        def complete(idx, arr, k):
            if idx == n:
                return ''
            i = (k-1)//(fact(len(arr))//len(arr))
            pick = arr.pop(i)
            k -= (i) * fact(len(arr))
            return pick + complete(idx+1, arr, k)

        return complete(0, arr, k)

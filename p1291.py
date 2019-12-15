class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        arr = [1,2,3,4,5,6,7,8,9]
        
        def solve(arr, start):
            n = arr[start]
            while n < high:
                if n >= low:
                    ans.append(n)
                n *= 10
                start += 1
                if start > 8:
                    break
                n += arr[start]
            
        for i in range(9):
            solve(arr, i)
        
        ans.sort()
        return ans
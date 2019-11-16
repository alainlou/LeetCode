class Solution:
    def encode(self, num: int) -> str:
        digits = 0
        left = 0
        right = 0        
        while right < num:
            digits += 1
            left = right+1
            right += int(math.pow(2, digits))
        answer = []
        while left != right:   
            mid = (right+left)//2
            if num > mid:
                answer.append('1')
                left = mid+1
            else:
                answer.append('0')
                right = mid
        return ''.join(answer)
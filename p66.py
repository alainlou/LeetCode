class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + 1 if digits[i] < 9 else 0
            if digits[i] != 0:
                carry = 0
                break
            carry = 1

        if carry:
            digits.insert(0, 1)

        return digits

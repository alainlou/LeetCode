class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lst = []
        while(head != None):
            lst.append(head.val)
            head = head.next
        ans = 0
        for i in range(len(lst)):
            ans += lst[-i-1] * pow(2, i)
        return ans
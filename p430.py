class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def solve(head):
            curr = head
            tail = head
            while curr:
                tail = curr
                if curr.child:
                    t = solve(curr.child)
                    tmp = curr.next
                    curr.next = curr.child
                    curr.child = None
                    curr.next.prev = curr
                    t.next = tmp
                    if tmp:
                        tmp.prev = t
                    curr = tmp
                    tail = t
                else:
                    curr = curr.next
            return tail

        solve(head)
        return head

from DS import ListNode

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        lst1head = head
        lst2head = head.next
        lst1head.next = None

        while lst2head:
            to_insert = lst2head
            lst2head = lst2head.next
            to_insert.next = None

            if lst1head.val > to_insert.val:
                to_insert.next = lst1head
                lst1head = to_insert
                continue

            curr = lst1head

            inserted = False
            while curr.next:
                if to_insert.val < curr.next.val:
                    to_insert.next = curr.next
                    curr.next = to_insert
                    inserted = True
                    break
                curr = curr.next

            if not inserted:
                curr.next = to_insert

        return lst1head

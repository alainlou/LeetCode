#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        bool carry = 0;
        while(curr) {
            int n = 0;
            n += l1 ? l1->val : 0;
            n += l2 ? l2->val : 0;
            n += carry;
            carry = n > 9 ? 1 : 0;
            n %= 10;
            curr->val = n;
            if((l1 && l1->next) || (l2 && l2->next) || carry)
                curr->next = new ListNode(0);
            curr = curr->next;
            l1 = l1 ? l1->next : NULL;
            l2 = l2 ? l2->next : NULL;
        }
        return head;
    }
};

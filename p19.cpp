#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head->next == NULL) {
            return NULL;
        }
        int length = 0;
        ListNode* curr = head;
        while(curr) {
            curr = curr->next;
            ++length;
        }
        int from_front = length - n;
        if(from_front == 0) {
            return head->next;
        }
        int index = 0;
        curr = head;
        while(curr) {
            if(index + 1 == from_front) {
                curr->next = curr->next->next;
                break;
            }
            curr = curr->next;
            ++index;
        }
        return head;
    }
};
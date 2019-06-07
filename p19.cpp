#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* look = head;
        for(int i = 0; i < n; ++i) {
            look = look->next;
        }
        while(look) {
            prev = curr;
            curr = curr->next;
            look = look->next;
        }
        if(!prev) {
            return head->next;
        } else {
            prev->next = curr->next;
            return head;
        }
    }
};
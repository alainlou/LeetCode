#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* tail = NULL;
        while(head) {
            ListNode* next = head->next;
            head->next = tail;
            tail = head;
            head = next;
        }
        return tail;
    }
};
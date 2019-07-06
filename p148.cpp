#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* merge(ListNode* left, ListNode* right) {
        // merge the two linked lists in order
        if(right == NULL)
            return left;
        ListNode* head;
        ListNode* end;
        ListNode* traverse1 = left;
        ListNode* traverse2 = right;
        if(left->val <= right->val) {
            head = left;
            end = head;
            traverse1 = traverse1->next;
        }
        else {
            head = right;
            end = head;
            traverse2 = traverse2->next;
        }
        while(traverse1 != NULL && traverse2 != NULL) {
            if(traverse1->val <= traverse2->val) {
                end->next = traverse1;
                traverse1 = traverse1->next;
                end = end->next;
            } else {
                end->next = traverse2;
                traverse2 = traverse2->next;
                end = end->next;
            }
        }
        while(traverse1 != NULL) {
            end->next = traverse1;
            traverse1 = traverse1->next;
            end = end->next;
        }
        while(traverse2 != NULL) {
            end->next = traverse2;
            traverse2 = traverse2->next;
            end = end->next;
        }
        return head;
    }
    ListNode* sortList(ListNode* head) {
        if(head == NULL)
            return NULL;
        else if(head->next == NULL)
            return head;
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* right = slow->next;
        slow->next = NULL;
        return merge(sortList(head), sortList(right));
    }
};
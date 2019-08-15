#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        // the odds
        ListNode* head1 = head;
        // the evens
        ListNode* head2 = head->next;
        
        ListNode* curr1 = head1;
        ListNode* curr2 = head2;
        while(curr1 != NULL && curr1->next != NULL && curr2 != NULL && curr2->next != NULL) {
            curr1->next = curr1->next->next;
            curr2->next = curr2->next->next;
            curr1 = curr1->next;
            curr2 = curr2->next;
        }
        while(curr1 != NULL && curr1->next != NULL) {
            curr1->next = curr1->next->next;
            curr1 = curr1->next;
        }
        while(curr2 != NULL && curr2->next != NULL) {
            curr2->next = curr2->next->next;
            curr2 = curr2->next;
        }
        
        // connect the two linked lists
        ListNode* result = head1;
        ListNode* traverse = result;
        while(traverse->next) {
            traverse = traverse->next;
        }
        traverse->next = head2;
        
        return result;        
    }
};

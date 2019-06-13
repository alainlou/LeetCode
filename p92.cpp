#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if(head -> next == NULL || m == n) {
            return head;
        }
        
        // Initializing the two pointers
        ListNode* left = head;
        ListNode* right = head;
        
        // Moving the two pointers to the start and end of the sublist
        for(int i = 1; i < m; ++i) {
            left = left->next;
        }
        for(int j = 1; j < n; ++j) {
            right = right->next;            
        }
        
        // Reversing the linked list in-place
        ListNode* prev = NULL;
        ListNode* curr = left;
        ListNode* next;
        while(curr != right) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr= next;
        }
        next = curr->next;
        curr->next = prev;
        
        // Inserting the reversed list (head is curr)
        // Case 1 it was the entire list
        // Case 2 the reversal happens on one of the ends
        // Case 3 it is somewhere in the middle

        // Case 1 or case 2
        if(left == head) {
            ListNode* traverse = curr;
            while(traverse->next) {
                traverse = traverse->next;
            }
            traverse->next = next;
            return curr;
        }
        
        // Case 3
        ListNode* traverse = head;
        while(traverse->next != left) {
            traverse = traverse->next;
        }
        traverse->next = curr;
        while(traverse->next) {
            traverse = traverse->next;
        }
        traverse->next = next;
        
        return head;
    }
};
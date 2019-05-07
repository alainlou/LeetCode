#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(!l1 && !l2){
            return NULL;
        }
        else if(l1 && !l2){
            return l1;
        }
        else if(l2 && !l1){
            return l2;
        }
        
        ListNode* before = new ListNode(0);
        ListNode* curr = new ListNode(0);
        
        if(l1->val < l2->val){
            curr = l1;
            l1 = l1->next;
        }
        else{
            curr = l2;
            l2 = l2->next;
        }
        
        before->next = curr;
        
        while(l1 && l2){        
            if(l1->val < l2->val){
                curr->next = l1;
                l1 = l1->next;
                curr = curr->next;
            }
            else{
                curr->next = l2;
                l2 = l2->next;
                curr = curr->next;
            }
        }
        while(l1){
            curr->next = l1;
            l1 = l1->next;
            curr = curr->next;
        }
        while(l2){
            curr->next = l2;
            l2 = l2->next;
            curr = curr->next;
        }
        
        return before->next;
    }
};
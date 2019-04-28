#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode * head = l1;
        while(l1 && l2){
            if(l1->val + l2->val < 10){
                l1->val += l2->val;
            }
            else{
                l1->val += l2->val - 10;
                if(l2->next){
                    l2->next->val += 1;
                    if(!l1->next){
                        l1->next = new ListNode(0);
                    }
                }
                else if(l1->next){
                    l1->next->val += 1;
                    if(!l2->next){
                        l2->next = new ListNode(0);
                    }
                }
                else{
                    l1->next = new ListNode(1);
                }
            }
            if(!(l1->next)){
                l1->next=l2->next;
                l2=NULL;
            }
            else{
                l1=l1->next;
                l2=l2->next;
            }
        }
        
        return head;
    }
};
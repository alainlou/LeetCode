#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode* reverse(ListNode* head) {
        ListNode* tail = NULL;
        while(head) {
            ListNode* next = head->next;
            head->next = tail;
            tail = head;
            head = next;
        }
        return tail;
    }
    bool isPalindrome(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        if(fast){
            slow = slow->next;
        }
        slow = reverse(slow);
        while(slow) {
            if(slow->val != head->val) {
                return false;
            }
            slow = slow->next;
            head = head->next;
        }
        return true;
    }
};
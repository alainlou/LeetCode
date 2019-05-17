#include <ListNode.hpp>
#include <bits/stdc++.h>

using namespace std;

class MinStack {
private:
    int minimum;
    ListNode* head;
public:
    MinStack() {
        minimum = INT_MAX;
        head = NULL;
    }
    
    void push(int x) {
        if(x < this->minimum) {
            minimum = x;
        }
        ListNode* node = new ListNode(x);
        node->next = head;
        head = node;
    }
    
    void pop() {
        head = head->next;
        minimum = INT_MAX;
        ListNode* curr = head;
        while(curr) {
            if(curr->val < minimum) {
                minimum = curr->val;
            }
            curr = curr->next;
        }
    }
    
    int top() {
        return head->val;
    }
    
    int getMin() {
        return minimum;
    }
};
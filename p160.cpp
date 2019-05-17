#include <ListNode.hpp>
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode *> nodes;
        while(headA) {
            nodes.insert(headA);
            headA = headA->next;
        }
        while(headB) {
            if(nodes.count(headB) > 0) {
                return headB;
            }
            headB = headB->next;
        }
        return NULL;
    }
};
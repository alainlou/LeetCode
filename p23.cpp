#include <bits/stdc++.h>
#include <ListNode.hpp>

using namespace std;

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* head;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        int k = lists.size();
        for(int i = 0; i < k; ++i) {
            if(lists[i] != NULL) {
                q.push({lists[i]->val, i});
                lists[i] = lists[i]->next;
            } 
        }
        if(q.empty())
            return NULL;
        pair<int, int> p = q.top();
        head = new ListNode(p.first);
        q.pop();
        if(lists[p.second] != NULL) {
            q.push({lists[p.second]->val, p.second});
            lists[p.second] = lists[p.second]->next;
        }  
        ListNode* curr = head;
        while(!q.empty()) {
            pair<int, int> p = q.top();
            curr->next = new ListNode(p.first);
            q.pop();
            if(lists[p.second] != NULL) {
                q.push({lists[p.second]->val, p.second});
                lists[p.second] = lists[p.second]->next;
            }  
            curr = curr->next;
        }
        return head;
    }
};

#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    map<int, int> counts;
    vector<int> findMode(TreeNode* root) {
        queue<TreeNode*> q;
        if(root != NULL)
            q.push(root);
        while(!q.empty()) {
            TreeNode* curr = q.front();
            ++counts[curr->val];
            if(curr->left != NULL) {
                q.push(curr->left);
            }
            if(curr->right != NULL) {
                q.push(curr->right);
            }
            q.pop();
        }
        int maximum = 0;
        vector<int> result;
        for(map<int, int>::iterator i = counts.begin(); i != counts.end(); ++i) {
            if(i->second > maximum) {
                result = {i->first};
                maximum = i->second;
            } else if (i->second == maximum) {
                result.push_back(i->first);
            }
        }
        return result;
    }
};
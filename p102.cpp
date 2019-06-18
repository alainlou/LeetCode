#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<pair<TreeNode*, int>> q;
        vector<vector<int>> result;
        if(root == NULL) {
            return result;
        }
        q.push({root, 0});
        while(!q.empty()) {
            TreeNode* curr = q.front().first;
            int level = q.front().second;
            if(level >= result.size()) {
                result.push_back({curr->val});
            } else {
                result[level].push_back(curr->val);
            }
            q.pop();
            if(curr->left != NULL) {
                q.push({curr->left, level + 1});
            }
            if(curr->right != NULL) {
                q.push({curr->right, level + 1});
            }   
        }
        return result;
    }
};
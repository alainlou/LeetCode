#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result = {{}};
        if(root == NULL) 
            return {};
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        int depth = 0;
        while(!q.empty()) {
            pair<TreeNode*, int> curr = q.front();
            if(curr.second > depth) {
                result.insert(result.begin(), {curr.first->val});
                ++depth;
            } else {
                result[0].push_back(curr.first->val);
            }
            if(curr.first->left != NULL)
                q.push({curr.first->left, depth + 1});
            if(curr.first->right != NULL)
                q.push({curr.first->right, depth + 1});
            q.pop();
        }
        return result;
    }
};
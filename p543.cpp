#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    map<TreeNode*, int> depths;
    int depth(TreeNode* root) {
        if(root == NULL) {
            return 0;
        } else if(depths[root]) {
            return depths[root];
        }
        int result = max(depth(root->left) + 1, depth(root->right) + 1);
        depths[root] = result;
        return result;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()) {
            if(!q.front()) {
                q.pop();
                continue;
            }
            TreeNode* curr = q.front();
            q.push(curr->left);
            q.push(curr->right);
            q.pop();
            diameter = max(diameter, depth(curr->left) + depth(curr->right));
        }
        return diameter;
    }
};
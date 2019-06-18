#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    int depth(TreeNode* root) {
        if(root == NULL) {
            return 0;
        }
        return max(depth(root->left) + 1, depth(root->right) + 1);
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
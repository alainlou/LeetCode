#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    bool traverse(TreeNode* root, long low, long high) {
        if(root == NULL)
            return true;
        if(root->val <= low || root->val >= high)
            return false;
        bool left = traverse(root->left, low, root->val);
        bool right = traverse(root->right, root->val, high);
        return left && right;
    }
    bool isValidBST(TreeNode* root) {
        return traverse(root, LONG_MIN, LONG_MAX);
    }
};
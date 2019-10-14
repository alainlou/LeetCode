#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        if(root == NULL)
            return true;
        if(root->left != NULL && root->left->val != root->val || !isUnivalTree(root->left))
             return false;
        if(root->right != NULL && root->right->val != root->val || !isUnivalTree(root->right))
            return false;
        return true;
    }
};

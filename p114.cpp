#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    void flatten(TreeNode* root) {
        if(root == NULL) {
            return;
        }
        flatten(root->left);
        flatten(root->right);
        if(!root->left) {
            return;
        }
        TreeNode* curr = root->left;
        while(curr->right) {
            curr = curr->right;
        }
        curr->right = root->right;        
        root->right = root->left;
        root->left = NULL;
    }
};
#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL)
            return NULL;
        TreeNode * left = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(left);
        return root;
    }
};
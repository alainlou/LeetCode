#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool pathSum(TreeNode* root, int sum) {
        if(root == NULL)
            return false;
        if(root->val == sum && root->left == NULL && root->right == NULL){
            return true;
        }
        return pathSum(root->left, sum-root->val) || pathSum(root->right, sum-root->val);
    }
    bool hasPathSum(TreeNode* root, int sum) {
        return pathSum(root, sum);
    }
};
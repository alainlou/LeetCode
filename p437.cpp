#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    int find(TreeNode* root, int &sum, int accumulate) {
        if(root == NULL) {
            return 0;
        }
        accumulate += root->val;
        if(accumulate == sum) {
            return 1 + find(root->left, sum, accumulate) + find(root->right, sum, accumulate);
        }
        else {
            return find(root->left, sum, accumulate) + find(root->right, sum, accumulate);
        }
    }
    int pathSum(TreeNode* root, int sum) {
        if(root == NULL) {
            return 0;
        }
        return find(root, sum, 0) + pathSum(root->left, sum) + pathSum(root->right, sum);
    }
};
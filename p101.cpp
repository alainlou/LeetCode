#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    bool checkSymmetric(TreeNode* left, TreeNode* right) {
        if(!left && !right) {
            return true;
        } else if(!left || !right) {
            return false;
        }
        return (left->val == right->val) 
            && checkSymmetric(left->left, right->right)
            && checkSymmetric(right->left, left->right);
    }
    bool isSymmetric(TreeNode* root) {
        return checkSymmetric(root, root);        
    }
};
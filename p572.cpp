#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool is_identical(TreeNode *one, TreeNode* two) {
        if(one == NULL && two == NULL)
            return true;
        else if(one == NULL || two == NULL)
            return false;
        else if(one->val != two->val)
            return false;
        else
            return is_identical(one->left, two->left) && is_identical(one->right, two->right);
    }
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(s == NULL) {
            return false;
        }
        return is_identical(s, t) || isSubtree(s->left, t) || isSubtree(s->right, t);
    }
};
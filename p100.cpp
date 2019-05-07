#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL){
            return true;
        }
        else if (p == NULL || q == NULL){
            return false;
        }
        else if (p->val != q->val){
            return false;
        }
        else{
            return isSameTree(p->right, q->right) && isSameTree(p->left, q->left);
        }
    }
};
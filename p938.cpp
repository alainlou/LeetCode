#include <bits/stdc++.h>
#include "TreeNode.hpp";

using namespace std;

class Solution {
public:
    void process(TreeNode* node, int& L, int& R, int& accumulate) {
        if(node == NULL)
            return;
        else if(node->val >= L && node->val <= R) {
            accumulate += node->val;
        }
        process(node->left, L, R, accumulate);
        process(node->right, L, R, accumulate);
    }
    int rangeSumBST(TreeNode* root, int L, int R) {
        int answer = 0;
        process(root, L, R, answer);
        return answer;
    }
};

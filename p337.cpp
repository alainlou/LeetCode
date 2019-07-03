#include <bits/stdc++.h>

using namespace std;

class Solution {
    unordered_map<TreeNode*, int> solution;
public:
    int rob(TreeNode* root) {
        if(root == NULL)
            return 0;
        else if(solution[root])
            return solution[root];
        int option1 = rob(root->left) + rob(root->right);
        int option2 = root->val;
        if(root->left)
            option2 += rob(root->left->left) + rob(root->left->right);
        if(root->right)
            option2 += rob(root->right->left) + rob(root->right->right);
        solution[root] = max(option1, option2);
        return solution[root];
    }
};
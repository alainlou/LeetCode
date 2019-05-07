#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root) {
            return 0;
        }
        return max(1 + maxDepth(root->left), 1 + maxDepth(root->right));
    }
};
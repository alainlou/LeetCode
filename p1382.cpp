#include <bits/stdc++.h>
#include "DS/TreeNode.hpp"

using namespace std;

class Solution {
private:
    vector<int> vals;
public:
    TreeNode* buildBST(int left, int right) {
        if (left == right)
            return NULL;
        int mid = (left+right)/2;
        return new TreeNode(vals[mid], buildBST(left, mid), buildBST(mid+1, right));
    }
    
    TreeNode* balanceBST(TreeNode* root) {
        dfs(root);
        
        return buildBST(0, vals.size());
    }
    
    void dfs(TreeNode* node) {
        if (node == NULL)
            return;
        dfs(node->left);
        vals.push_back(node->val);
        dfs(node->right);        
    }
};
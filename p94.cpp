#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    void add(TreeNode* root, vector<int>& vec) {
        if(root == NULL) {
            return;
        } else if(root->left == NULL && root->right == NULL) {
            vec.push_back(root->val);
        }
        else {
            add(root->left, vec);
            vec.push_back(root->val);
            add(root->right, vec);
        }
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        add(root, result);
        return result;
    }
};
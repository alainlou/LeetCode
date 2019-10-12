#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> subvec(vector<int>& vec, int start, int end) {
        vector<int> result(vec.begin()+start, vec.begin()+end);
        return result;
    }
    TreeNode* buildTree(vector<int> preorder, vector<int> inorder) {
        if(preorder.size() == 0 || inorder.size() == 0)
            return NULL;
        TreeNode *root = new TreeNode(preorder[0]);
        int index;
        for(int i = 0; i < inorder.size(); ++i) {
            if(inorder[i] == preorder[0]) {
                index = i;
                break;
            }
        }
        root->left = buildTree(subvec(preorder, 1, index+1), subvec(inorder, 0, index));
        root->right = buildTree(subvec(preorder, index+1, preorder.size()), subvec(inorder, index+1, inorder.size()));
        return root;
    }
};

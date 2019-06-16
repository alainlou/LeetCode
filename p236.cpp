#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    TreeNode* answer;
    bool traverse(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL) {
            return false;
        }
        bool mid = root == p || root == q;
        bool left = traverse(root->left, p, q);
        bool right = traverse(root->right, p, q);
        if(mid + left + right >= 2) {
            answer = root;
        }
        return (mid + left + right > 0);
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        traverse(root, p, q);
        return answer;
    }
};
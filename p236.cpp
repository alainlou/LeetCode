#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool find(TreeNode* root, TreeNode* node, map<TreeNode*, bool>& vec) {
        if(root == NULL) {
            vec[root] = false;
            return false;
        } else if(root == node) {
            vec[root] = true;
            return true;
        }
        bool result = find(root->left, node, vec) || find(root->right, node, vec);
        vec[root] = result;
        return result;
    }
    void find_lowest(TreeNode* root, TreeNode* p, TreeNode * q, map<TreeNode*, bool> p_included, map<TreeNode*, bool> q_included, TreeNode*& answer) {
        if(root == NULL) {
            return;
        }
        if(p_included[root] && q_included[root] && 
           !(p_included[root->left] && q_included[root->left]) &&
           !(p_included[root->right] && q_included[root->right])) {
               answer = root;
           }
        find_lowest(root->left, p, q, p_included, q_included, answer);
        find_lowest(root->right, p, q, p_included, q_included, answer);
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        map<TreeNode*, bool> p_included;
        map<TreeNode*, bool> q_included;
        find(root, p, p_included);
        find(root, q, q_included);
        //traverse and find the lowest
        TreeNode* answer;
        find_lowest(root, p, q, p_included, q_included, answer);
        return answer;
    }
};
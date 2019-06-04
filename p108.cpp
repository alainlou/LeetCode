#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    TreeNode* process(vector<int>& nums, int start, int end) {
        if(start > end) {
            return NULL;
        }
        int mid = (start+end)/2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = process(nums, start, mid - 1);
        root->right = process(nums, mid+1, end);
        return root;
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if(nums.size() < 1) {
            return NULL;
        }
        return process(nums, 0, nums.size() - 1);
    }
};
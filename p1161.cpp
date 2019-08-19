#include <bits/stdc++.h>
#include <TreeNode.hpp>

using namespace std;

class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        map<int, int> sums;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 1});
        int depth = 0;
        while(!q.empty()) {
            TreeNode* curr = q.front().first;
            depth = q.front().second;
            sums[q.front().second] += curr->val;
            if(curr->left != NULL)
                q.push({curr->left, q.front().second+1});
            if(curr->right != NULL)
                q.push({curr->right, q.front().second+1});
            q.pop();
        }
        int answer = INT_MIN;
        int level = INT_MAX;
        for(int i = depth; i >= 0; --i) {
            if(sums[i] > answer) {
                answer = sums[i];
                level = i;
            }
        }
        return level;
    }
};

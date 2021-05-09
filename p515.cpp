#include <bits/stdc++.h>
#include "DS/TreeNode.hpp"

using namespace std;

class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        if (root == NULL)
            return {};

        queue<pair<TreeNode *, int>> q;
        q.push({root, 0});
        int curr_level = 0;
        int curr_max = INT_MIN;
        vector<int> ans;

        while(q.size() > 0) {
            pair<TreeNode *, int> curr = q.front();
            q.pop();
            if (curr.second > curr_level) {
                curr_level = curr.second;
                ans.push_back(curr_max);
                curr_max = INT_MIN;
            }
            curr_max = max(curr_max, curr.first->val);
            if (curr.first->left)
                q.push({curr.first->left, curr_level+1});
            if (curr.first->right)
                q.push({curr.first->right, curr_level+1});
        }

        ans.push_back(curr_max);

        return ans;
    }
};

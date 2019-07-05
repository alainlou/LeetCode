#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int smallest = INT_MAX;
        int largest = INT_MIN;
        // counting sort
        for(int n : nums) {
            smallest = min(n, smallest);
            largest = max(n, largest);
        }
        int counts[largest-smallest+1];
        memset(counts, 0, sizeof(counts));
        for(int n : nums) {
            ++counts[n-smallest];
        }
        vector<int> copy;
        for(int i = 0; i < largest-smallest+1; ++i) {
            for(int j = 0; j < counts[i]; ++j) {
                copy.push_back(i+smallest);
            }
        }
        // set to if you don't need to sort it
        int start = 0;
        int end = 0;
        // find the start
        for(int i = 0; i < nums.size(); ++i) {
            if(copy[i] != nums[i]) {
                start = i;
                break;
            }
        }
        // find the end
        for(int j = nums.size()-1; j >= 0; --j) {
            if(copy[j] != nums[j]) {
                end = j+1;
                break;
            }
        }
        return end-start;
    }
};
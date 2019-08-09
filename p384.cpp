#include <bits/stdc++.h>

using namespace std;

class Solution {
private:
    int n;
    vector<int> original;
public:
    Solution(vector<int>& nums) {
        n = nums.size();
        original = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return original;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> shuffled = original;
        int n = shuffled.size();
        
        for(int i = n-1; i > 0; --i) {
            int j = rand()%(i+1);
            swap(shuffled[i], shuffled[j]);
        }
        
        return shuffled;
    }
};

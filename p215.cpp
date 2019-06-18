#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int minimum = INT_MAX;
        int maximum = INT_MIN;
        // finding the minimum and maximum
        for(int n : nums) {
            minimum = min(minimum, n);
            maximum = max(maximum, n);
        }
        // number of elements in the count array
        int n = maximum - minimum + 1;
        int * count = new int[n];
        memset(count, 0, n*sizeof(int));
        for(int num : nums) {
            ++count[num - minimum];
        }
        int counter = 0;
        for(int i = n - 1; i >= 0; --i) {
            counter += count[i];
            if(counter >= k) {
                return i + minimum;
            }
        }
        return -1;
    }
};
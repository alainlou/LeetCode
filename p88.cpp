#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i, j;
        i = j = 0;
        while(i < m && j < n) {
            if(nums1[i] >= nums2[j]) {
                for(int k {nums1.size()-1}; k > i; --k) {
                    nums1[k] = nums1[k-1];
                }
                nums1[i] = nums2[j++];
                ++m;
            } else {
                ++i;
            }
        }
        while(j < n) {
            nums1[i++] = nums2[j++];
        }
    }
};
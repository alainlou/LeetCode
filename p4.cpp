#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int incr = 0;
        vector<int> nums(nums1.size()+nums2.size(), 0);
        int p1 = 0;
        int p2 = 0;
        while(p1 < nums1.size() && p2 < nums2.size()) {
            if(nums1[p1] < nums2[p2])
                nums[incr++] = nums1[p1++];
            else
                nums[incr++] = nums2[p2++];
        }
        while(p1 < nums1.size()) {
            nums[incr++] = nums1[p1++];
        }
        while(p2 < nums2.size()) {
            nums[incr++] = nums2[p2++];
        }
        if(nums.size()%2 == 0)
            return (nums[nums.size()/2] + nums[nums.size()/2-1])/2.0;
        else
            return nums[nums.size()/2];
    }
};

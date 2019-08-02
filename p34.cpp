#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        // size one edge case
        if(nums.size() == 1) {
            if(nums[0] == target)
                return {0, 0};
            else
                return {-1, -1};
        }
        // find start point
        int start = -1;
        int n = nums.size();
        int left = 0;
        int right = n;
        int mid = right/2;
        while(left < right) {
            if(nums[mid] == target && (mid == 0 || nums[mid-1] < target)) {
                start = mid;
                break;
            } else if(left == mid || right == mid) {
                break;
            } else if(nums[mid] >= target) {
                right = mid;
                mid = (left + right)/2;
            } else {
                left = mid;
                mid = (left + right)/2;
            }
        }
        // find end point
        int end = -1;
        left = 0;
        right = n;
        mid = right/2;
        while(left < right) {
            if(nums[mid] == target && (mid == n-1 || nums[mid+1] > target)) {
                end = mid;
                break;
            } else if (left == mid || right == mid) {
                break;
            } else if(nums[mid] <= target) {
                left = mid;
                mid = (left + right)/2;
            } else {
                right = mid;
                mid = (left + right)/2;
            }
        }
        return {start, end};
    }
};
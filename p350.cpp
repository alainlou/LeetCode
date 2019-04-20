#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> count;
        for(int num : nums1) {
            ++count[num];
        }
        vector<int> intersect;
        for(int num : nums2){
            if(count.count(num) > 0 && count[num] > 0){
                intersect.push_back(num);
                --count[num];
            }
        }
        return intersect;
    }
};
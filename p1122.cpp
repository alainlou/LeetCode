#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> order;
        unordered_map<int, int> value;
        for(int i = 0; i < arr2.size(); ++i) {
            order[arr2[i]] = i;
            value[i] = arr2[i];
        }
        int counts[1001];
        int extra[1001];
        memset(counts, 0, sizeof(counts));
        memset(extra, 0, sizeof(extra));
        for(int i : arr1) {
            if(order.find(i) != order.end())
                ++counts[order[i]];
            else
                ++extra[i];
        }
        
        vector<int> answer(arr1.size());
        int iter = 0;
        
        for(int i = 0; i < 1001; ++i) {
            while(counts[i] > 0) {
                answer[iter] = value[i];
                --counts[i];
                ++iter;
            }
        }
        for(int i = 0; i < 1001; ++i) {
            while(extra[i] > 0) {
                answer[iter] = i;
                --extra[i];
                ++iter;
            }
        }
        
        return answer;
    }
};

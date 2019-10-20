#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& arr) {
        int d = arr[1]-arr[0];
        for(int i = 2; i < arr.size(); ++i) {
            if(abs(arr[i]-arr[i-1]) < abs(d))
                d = arr[i]-arr[i-1];
        }
        for(int i = 1; i < arr.size(); ++i) {
            if(arr[i]-arr[i-1] != d)
                return arr[i-1]+d;
        }
        return 0;
    }
};

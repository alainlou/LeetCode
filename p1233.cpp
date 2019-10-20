#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isChild(string higher, string lower) {
        if(higher.size() > lower.size())
            return false;
        int i = 0;
        while(i < higher.size()) {
            if(higher[i] != lower[i])
                return false;
            ++i;
        }
        return i < lower.size() && lower[i] == '/';
    }
    vector<string> removeSubfolders(vector<string>& folder) {
        sort(folder.begin(), folder.end());
        int left = 0;
        int right = 1;
        vector<string> answer;
        answer.push_back(folder[0]);
        while(left < folder.size() && right < folder.size()) {
            while(right < folder.size() && isChild(folder[left], folder[right])) {
                ++right;
            }
            if(right < folder.size()) {
                answer.push_back(folder[right]);
                left = right;
                right = left + 1;
            }            
        }
        return answer;
    }
};

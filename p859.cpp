#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool buddyStrings(string A, string B) {
        if(A.size() != B.size())
            return false;
        int count = 0;
        vector<int> counts1(26, 0);
        vector<int> counts2(26, 0);
        pair<char, char> diff1;
        pair<char, char> diff2;
        for(int i = 0; i < A.size(); ++i) {
            ++counts1[A[i]-'a'];
            ++counts2[A[i]-'a'];
            if(A[i] != B[i]) {
                if(count == 2) {
                    return false;
                } else if(count == 0) {
                    diff1.first = A[i];
                    diff1.second = B[i];
                    ++count;
                } else if(count == 1) {
                    diff2.first = A[i];
                    diff2.second = B[i];
                    ++count;
                }
            }
        }
        bool free = false;
        for(int i = 0; i < 26; ++i) {
            if(counts1[i] >= 2 || counts2[i] >= 2) {
                free = true;
                break;
            }
        }
        return (count == 0 && free) || (count == 2 && diff1.first == diff2.second && diff1.second == diff2.first);
    }
};

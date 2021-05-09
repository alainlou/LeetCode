#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        vector<int> indices;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};

        for(int i = 0; i < s.size(); ++i) {
            if (vowels.count(tolower(s[i])) > 0) {
                indices.push_back(i);
            }
        }

        for(int i = 0; i < indices.size()/2; ++i) {
            char tmp = s[indices[i]];
            s[indices[i]] = s[indices[indices.size()-1-i]];
            s[indices[indices.size()-1-i]] = tmp;
        }

        return s;
    }
};

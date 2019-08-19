#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool possible(string word, string chars) {
        int counts[26];
        memset(counts, 0, sizeof(counts));
        for(char c : chars) {
            ++counts[c-'a'];
        }
        for(char c : word) {
            if(counts[c-'a'] == 0)
                return false;
            --counts[c-'a'];
        }
        return true;
    }
    int countCharacters(vector<string>& words, string chars) {
        int answer = 0;
        for(string word : words) {
            if(possible(word, chars)) {
                answer += word.size();
            }
        }
        return answer;
    }
};
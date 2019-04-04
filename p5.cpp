#include <bits/stdc++.h>;

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        bool value = true;
        int len = s.length();
        for(int i = 0; i < len; i++){
            if(s[i] != s[len-1-i]){
                value = false;
                break;
            }
        }
        return value;
    }
    
    string longestPalindrome(string s) {
        string toReturn = "";
        int len = s.length();
        for(int i = len; i > 0; i--){
            int start = 0;
            while(start + i <= len){
                if(isPalindrome(s.substr(start, i))){
                    return s.substr(start, i);
                }
                start++;
            }
        }
        return toReturn;
    }
};
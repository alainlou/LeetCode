#include <bits/stdc++.h>

using namespace std;

class Solution {
public:    
    string longestPalindrome(string s) {
        int size = s.size();
        if(size == 0){
            return "";
        }
        string answer = s.substr(0,1);
        int max_length = 1;
        
        bool isPalindrome [size][size];
        memset(isPalindrome, false, sizeof(isPalindrome));
        
        // Length 1
        for(int i = 0; i < size; ++i){
            isPalindrome[i][i] = true;
        }
        
        // Length 2
        for(int j = 0; j < size - 1; ++j){
            if(s[j] == s[j+1]){
                isPalindrome[j][j+1] = true;
                max_length = 2;
                answer = s.substr(j, 2);
            }
        }
        
        // 3 to n
        for(int k = 2; k <= size; ++k){
            for(int l = 0; l < size - k; ++l){
                if(isPalindrome[l+1][l+k-1] && s[l] == s[l+k]){
                    isPalindrome[l][l+k] = true;
                    if(k+1 > max_length){
                        max_length = k+1;
                        answer = s.substr(l, k+1);
                    }
                }
            }
        }
        
        return answer;
    }
};
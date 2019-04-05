#include <bits/stdc++.h>;

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        string answer = "";
        vector<int> numbers {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> strs {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        for(size_t iter = 0; iter < numbers.size(); ++iter){
            int i = numbers[iter];
            string str = strs[iter];
            
            while(num >= i){
                answer += str;
                num -= i;
            }
        }
        return answer;
    }
};
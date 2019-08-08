#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string defangIPaddr(string address) {
        for(int i = 0; i < address.size(); ++i) {
           if(address[i] == '.') {
               address[i] = '[';
               address.insert(i+1, ".");
               address.insert(i+2, "]");
               i += 3;
           }
        }
        return address;
    }
};

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int cooldown[26];
        memset(cooldown, 0, sizeof(cooldown));
        int count[26];
        int total = 0;
        memset(count, 0, sizeof(count));
        for(char c : tasks) {
            ++count[c-'A'];
            ++total;
        }
        
        int answer = 0;
        
        // start doing the tasks
        while(total > 0) {
            // always pick the one with the greatest count
            int highest = INT_MIN;
            int select = -1;
            for(int i = 0; i < 26; ++i) {
                if(count[i] > 0 && count[i] > highest && cooldown[i] == 0) {
                    select = i;
                    highest = count[i];
                }
            }
            if(select != -1) {
                --count[select];
                --total;
                cooldown[select] = n+1;
            }
            for(int j = 0; j < 26; ++j) {
                if(cooldown[j] > 0)
                    --cooldown[j];
            }
            ++answer;
        }
        
        return answer;
    }
};

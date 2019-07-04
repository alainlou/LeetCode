#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        map<int, int> count;
        for(int n : nums) {
            ++count[n];
        }
        if(count.size() == 0)
            return 0;
        else if(count.size() == 1)
            return 1;
        map<int, int>::iterator iter = count.begin();
        int previous = iter->first;
        int longest = 0;
        int streak = 1;
        ++iter;
        for(map<int, int>::iterator i = iter; i != count.end(); ++i) {
            if(i->first == previous+1)
                ++streak;
            else
                streak = 1;
            previous = i->first;
            longest = max(longest, streak);
        }
        return longest;
    }
};
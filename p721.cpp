#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        vector<vector<string>> result;
        vector<int> to_delete;
        map<string, pair<string, int>> profiles;
        for(int a = 0; a < accounts.size(); ++a) {
            sort(accounts[a].begin(), accounts[a].end());
        }
        sort(accounts.begin(), accounts.end());
        for(int i = 0; i < accounts.size(); ++i) {
            vector<string> account = accounts[i];
            bool found = false;
            int index;
            string name = account[0];
            for(int j = 1; j < account.size(); ++j) {
                if(profiles[account[j]].first == name && profiles[account[j]].second != i) {
                    found = true;
                    index = profiles[account[j]].second;
                    break;
                }
                profiles[account[j]] = {name, i};
            }
            if(found) {
                for(int k = 1; k < account.size(); ++k) {
                    if(profiles[account[k]].second == i) {
                        profiles[account[k]] = {name, index};
                    }
                    // recognize a duplicate here
                    accounts[index].push_back(account[k]);
                }
                accounts.erase(accounts.begin() + i);
                cout << i << ", " << index << "; ";
                i = index;
            }
        }
        for(int a = 0; a < accounts.size(); ++a) {
            sort(accounts[a].begin() + 1, accounts[a].end());
            for(int b = 2; b < accounts[a].size(); ++b) {
                if(accounts[a][b-1] == accounts[a][b]) {
                    accounts[a].erase(accounts[a].begin() + b - 1);
                    --b;
                }
            }
        }
        return accounts;         
    }
};
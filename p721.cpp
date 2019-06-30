#include <bits/stdc++.h>

using namespace std;

struct DisjointSet {
    int parent[10000];
    DisjointSet() {
        for(int i = 0; i < 10000; ++i) {
            parent[i] = i;
        }
    }
    int find(int i) {
        if(parent[i] != i)
            parent[i] = find(parent[i]);
        return parent[i];
    }
    void merge(int i, int j) {
        parent[find(i)] = find(j);
    }
};
class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        DisjointSet ds;
        unordered_map<string, int> email_to_id;
        unordered_map<string, string> email_to_name;
        int id = 0;
        for(vector<string> row : accounts) {
            string name = row[0];
            for(int i = 1; i < row.size(); ++i) {
                string email = row[i];
                email_to_name[email] = name;
                if(email_to_id.find(email) == email_to_id.end()) {
                    email_to_id[email] = id++;
                }
                ds.merge(email_to_id[row[1]], email_to_id[email]);
            }
        }
        unordered_map<int, vector<string>> answer;
        for(auto i = email_to_id.begin(); i != email_to_id.end(); ++i) {
            int index = ds.find(email_to_id[i->first]);
            if(answer.find(index) == answer.end()) {
                answer[index] = {i->first};
            } else {
                answer[index].push_back(i->first);
            }
        }
        vector<vector<string>> result;
        for(auto j = answer.begin(); j != answer.end(); ++j) {
            vector<string> account = j->second;
            sort(account.begin(), account.end());
            vector<string> row = {email_to_name[account[0]]};
            row.insert(row.end(), account.begin(), account.end());
            result.push_back(row);
        }
        return result;
    }
};
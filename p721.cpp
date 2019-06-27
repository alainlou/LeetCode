#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        map<string, int> parent;
        map<int, string> id_to_name;
        int id = 0;
        // put the accounts into maps for parent and id_to_name
        for(vector<string> account : accounts) {
            int union_into = -1;
            set<int> to_combine;
            string name = account[0];
            id_to_name[id] = name;
            for(int i = 1; i < account.size(); ++i) {
                string email = account[i];
                if(parent.find(email) != parent.end() && parent[email] != id) {
                    if(union_into == -1)
                        union_into = parent[email];
                    else
                        to_combine.insert(parent[email]);
                }
                parent[email] = id;
            }
            // perform the union
            if(union_into > -1) {
                for(int i = 1; i < account.size(); ++i) {
                    string email = account[i];
                    parent[email] = union_into;
                }
                for(map<string, int>::iterator iter = parent.begin(); iter != parent.end(); ++iter) {
                    if(to_combine.find(iter->second) != to_combine.end()) {
                        parent[iter->first] = union_into;
                    }
                }
            }
            ++id;
        }
        map<int, vector<string>> id_with_emails;
        // create a map with key id and value vector of emails
        for(map<string, int>::iterator iter = parent.begin(); iter != parent.end(); ++iter) {
            if(id_with_emails.find(iter->second) == id_with_emails.end())
                id_with_emails[iter->second] = {iter->first};
            else
                id_with_emails[iter->second].push_back(iter->first);
        }
        vector<vector<string>> result;
        for(map<int, vector<string>>::iterator iter = id_with_emails.begin(); iter != id_with_emails.end(); ++iter) {
            vector<string> entry;
            entry.push_back(id_to_name[iter->first]);
            for(string email : iter->second) {
                entry.push_back(email);
            }
            result.push_back(entry);
        }
        // read from the parent and collect the emails that share the same parent
        return result;
    }
};
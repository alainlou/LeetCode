#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, set<int>> parents;
        unordered_map<int, set<int>> children;
        // fill parent and children maps
        for(vector<int> edge: prerequisites) {
            if(parents.find(edge[0]) != parents.end())
                parents[edge[0]].insert(edge[1]);
            else
                parents[edge[0]] = {edge[1]};
            if(children.find(edge[1]) != children.end())
                children[edge[1]].insert(edge[0]);
            else
                children[edge[1]] = {edge[0]};
        }
        queue<int> q;
        // enqueue courses without prereq
        for(int i = 0; i < numCourses; ++i) {
            if(parents.find(i) == parents.end())
                q.push(i);
        }
        vector<int> result;
        vector<int> empty;
        while(!q.empty()) {
            int curr = q.front();
            result.push_back(curr);
            for(int child : children[curr]) {
                parents[child].erase(curr);
                if(parents[child].empty())
                    q.push(child);
            }
            q.pop();
        }
        return (result.size() == numCourses) ? result : empty;
    }
};
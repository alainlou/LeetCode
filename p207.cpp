#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
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
        int result = 0;
        for(int i = 1; i < numCourses; ++i) {
            result += i;
        }
        while(!q.empty()) {
            int curr = q.front();
            result -= curr;
            for(int child : children[curr]) {
                parents[child].erase(curr);
                if(parents[child].empty())
                    q.push(child);
            }
            q.pop();
        }
        return result == 0;
    }
};
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> gardenNoAdj(int N, vector<vector<int>>& paths) {
        map<int, set<int>> surrounding;
        vector<int> answer;
        for(vector<int> path : paths) {
            surrounding[path[0]-1].insert(path[1]-1);
            surrounding[path[1]-1].insert(path[0]-1);
        }
        set<int> visited;
        for(int i = 0; i < N; ++i) {
            if(visited.find(i) == visited.end()) {
                set<int> existing;
                visited.insert(i);
                for(int node : surrounding[i]) {
                    if(node < answer.size())
                        existing.insert(answer[node]);
                }
                for(int j = 1; j < 5; ++j) {
                    if(existing.find(j) == existing.end()) {
                        answer.push_back(j);
                        break;
                    }
                }
            }
        }
        return answer;
    }
};
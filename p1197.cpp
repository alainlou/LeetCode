#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minKnightMoves(int x, int y) {
        bool visited[800][800];
        memset(visited, false, sizeof(visited));
        queue<pair<pair<int,int>,int>> q;
        q.push({{400,400}, 0});
        x += 400;
        y += 400;
        while(!q.empty()) {
            pair<int, int> position = q.front().first;
            if(visited[position.first][position.second]) {
                q.pop();
                continue;
            }
            visited[position.first][position.second] = true;
            int move_number = q.front().second;
            if(position.first == x && position.second == y)
                return move_number;
            int a = position.first;
            int b = position.second;
            q.pop();
            if(!visited[a+2][b+1]) {
                q.push({{a+2, b+1}, move_number+1});
            }
            if(!visited[a+2][b-1]) {
                q.push({{a+2, b-1}, move_number+1});
            }
            if(!visited[a+1][b+2]) {
                q.push({{a+1, b+2}, move_number+1});
            }
            if(!visited[a+1][b-2]) {
                q.push({{a+1, b-2}, move_number+1});
            }
            if(!visited[a-1][b+2]) {
                q.push({{a-1, b+2}, move_number+1});
            }
            if(!visited[a-1][b-2]) {
                q.push({{a-1, b-2}, move_number+1});
            }
            if(!visited[a-2][b+1]) {
                q.push({{a-2, b+1}, move_number+1});
            }
            if(!visited[a-2][b-1]) {
                q.push({{a-2, b-1}, move_number+1});
            }   
        }
        return -1;
    }
};

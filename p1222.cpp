#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        vector<vector<int>> answer;
        bool board[8][8];
        memset(board, false, sizeof(board));
        for(vector<int> coordinate : queens) {
            board[coordinate[0]][coordinate[1]] = true;
        }
        int x0 = king[0];
        int y0 = king[1];
        for(int y = y0; y >= 0; --y) {
            if(board[x0][y]) {
                answer.push_back({x0, y});
                break;
            }
        }
        for(int y = y0; y < 8; ++y) {
            if(board[x0][y]) {
                answer.push_back({x0, y});
                break;
            }
        }
        for(int x = x0; x >= 0; --x) {
            if(board[x][y0]) {
                answer.push_back({x, y0});
                break;
            }
        }
        for(int x = x0; x < 8; ++x) {
            if(board[x][y0]) {
                answer.push_back({x, y0});
                break;
            }
        }
        int x = x0;
        int y = y0;
        while(x >= 0 && y >= 0) {
            if(board[x][y]) {
                answer.push_back({x, y});
                break;
            }
            --x;
            --y;
        }
        x = x0;
        y = y0;
        while(x < 8 && y < 8) {
            if(board[x][y]) {
                answer.push_back({x, y});
                break;
            }
            ++x;
            ++y;
        }
        x = x0;
        y = y0;
        while(x < 8 && y >= 0) {
            if(board[x][y]) {
                answer.push_back({x, y});
                break;
            }
            ++x;
            --y;
        }
        x = x0;
        y = y0;
        while(x >= 0 && y < 8) {
            if(board[x][y]) {
                answer.push_back({x, y});
                break;
            }
            --x;
            ++y;
        }
        return answer;
    }
};

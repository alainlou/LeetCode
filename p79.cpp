#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool search(vector<vector<char>>& board, string& word, int i, int row, int col) {
        // out of bounds
        if(row >= board.size() || row < 0)
            return false;
        if(col >= board[0].size() || col < 0)
            return false;
        // found the word
        if(i == word.size()-1 && board[row][col] == word[word.size()-1])
            return true;
        // not the right letter or already visited
        if(board[row][col] != word[i])
            return false;
        // fill it so we don't cycle back
        char c = board[row][col];
        board[row][col] = ' ';
        bool answer = search(board, word, i+1, row, col-1) || search(board, word, i+1, row, col+1)|| search(board, word, i+1, row-1, col) || search(board, word, i+1, row+1, col); 
        // reset the cell
        board[row][col] = c;
        return answer;
    }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i = 0; i < board.size(); ++i) {
            for(int j = 0; j < board[0].size(); ++j) {
                if(search(board, word, 0, i, j)) {
                    return true;
                }
            }
        }
        return false;
    }
};
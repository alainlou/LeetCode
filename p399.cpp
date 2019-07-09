#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        // mapping from string to int
        unordered_map<string, int> var_to_int;
        int increment = 0;
        for(vector<string> equation : equations) {
            for(string var : equation) {
                if(var_to_int.find(var) == var_to_int.end()) {
                    var_to_int[var] = increment++;
                }
            }
        }
        int n = equations.size();
        double comp[increment][increment];
        for(int i = 0; i < increment; ++i) {
            for(int j = 0; j < increment; ++j) {
                // a number divided by itself is 1
                if(i == j)
                    comp[i][j] = 1;
                // assign -1 by default (we don't know)
                else
                    comp[i][j] = -1;
            }
        }
        for(int i = 0; i < n; ++i) {
            vector<string> equation = equations[i];
            double value = values[i];
            comp[var_to_int[equation[0]]][var_to_int[equation[1]]] = value;
            comp[var_to_int[equation[1]]][var_to_int[equation[0]]] = 1/value;
        }
        // Floyd-Warshall
        for(int i = 0 ; i < increment; ++i) {
            for(int j = 0; j < increment; ++j) {
                for(int k = 0; k < increment; ++k) {
                    if(comp[i][j] != -1 && comp[j][k] != -1) {
                        comp[i][k] = comp[i][j] * comp[j][k];
                        comp[k][i] = 1/comp[i][k];
                    }
                }
            }
        }
        vector<double> results;
        // read the expressions
        for(vector<string> q : queries) {
            string a = q[0];
            string b = q[1];
            // check they are in bounds
            if(var_to_int.find(a) == var_to_int.end() || var_to_int.find(b) == var_to_int.end()) {
                results.push_back(-1);
            } else {
                int x = var_to_int[a];
                int y = var_to_int[b];
                results.push_back(comp[x][y]);
            }
        }
        return results;
    }
};
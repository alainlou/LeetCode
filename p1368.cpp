class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<bool>> visited(m, vector<bool>(n, false));
        priority_queue<vector<int>> q;
        q.push({0, 0, 0});

        while (true) {
            vector<int> t = q.top();
            int i = t[1];
            int j = t[2];
            int cost = t[0];
            visited[i][j] = true;
            q.pop();

            // We got to the end
            if (i == m-1 && j == n-1) {
                // We stored the negative cost in our priority queue
                return -cost;
            }

			// Direction
            int d = grid[i][j];

            // Add to the priority queue
            // (note that C++ uses a max queue, not min queue)
            if (j+1 < n && !visited[i][j+1]) {
                int c = d == 1 ? cost : cost - 1;
                q.push({c, i, j+1});
            }
            if (j-1 >= 0 && !visited[i][j-1]) {
                int c = d == 2 ? cost : cost - 1;
                q.push({c, i, j-1});
            }
            if (i+1 < m && !visited[i+1][j]) {
                int c = d == 3 ? cost : cost - 1;
                q.push({c, i+1, j});
            }
            if (i-1 >= 0 && !visited[i-1][j]) {
                int c = d == 4 ? cost : cost - 1;
                q.push({c, i-1, j});
            }
        }

        return -1;
    }
};

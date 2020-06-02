#include <bits/stdc++.h>

using namespace std;

struct DSU {
    int parent[10];
    DSU() {
        for(int i = 0; i < 10; ++i) {
            parent[i] = i;
        }
    }
    int find(int i) {
        if(parent[i] != i) {
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }
    void combine(int i, int j) {
        parent[find(i)] = parent[j];
    }
    void print() {
        for(int i = 0; i < 10; ++i) {
            cout << parent[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    DSU dsu;
    dsu.print();
    dsu.combine(1, 2);
    dsu.combine(1, 5);
    dsu.print();
    return 0;
}

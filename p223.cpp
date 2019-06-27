#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int area = 0;
        // make ABCD the rectangle on the left
        if(A > E) {
            swap(A, E);
            swap(B, F);
            swap(C, G);
            swap(D, H);
        }
        bool x_overlap = A <= E && E <= C;
        // overlap on one side or on both sides
        bool y_overlap = (H > B && H <= D) || (F < D && F >= B) || (H > D && F < B);
        if(x_overlap && y_overlap){
            int width = min(C, G) - E;
            int height = min(D, H) - max(B, F);
            area -= width * height;
        }
        area += (C-A)*(D-B);
        area += (G-E)*(H-F);
        return area;
    }
};
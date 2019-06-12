#include <iostream>
#include <cstddef>
#include <vector>
#include <algorithm>

using namespace std;

void print_vec(vector<int> &vec) {
    cout << "[ ";
    for(int i : vec) {
        cout << i << " ";
    }
    cout << "]" << endl;
}

int partition(vector<int> &vec, int left, int right) {
    // pick the pivot value
    int pivot = vec[right];
    // swaping elements from the right and left
    while(left < right) {
        // stop on when we need to move something to the right
        while(vec[left] < pivot) {
            ++left;
        }
        // stop on when we need to move something to the left
        while(vec[right] > pivot) {
            --right;
        }
        // check that they are still on the left and right halfs
        if(left < right) {
            int swp = vec[left];
            vec[left] = vec[right];
            vec[right] = swp;
            ++left;
            --right;
        }
    }
    // everything "left" and to the right is greater than the pivot value
    return left;
}

void quicksort(vector<int> &vec, int left, int right) {
    // start of the right (all elements in the right are greater than all elements of the left)
    int div = partition(vec, left, right);
    // this block is a sorted subarray
    if(div == left) {
        return;
    }
    // sort the left side
    quicksort(vec, left, div - 1);
    // sort the right side
    quicksort(vec, div, right);
}

void quicksort(vector<int> &vec) {
    quicksort(vec, 0, vec.size() - 1);
}

int main() {
    vector<int> vec = {0, 9, -2, -8, -9, 8, 7, 6, 5, 4, 3, 2, 1};
    print_vec(vec);
    quicksort(vec);
    print_vec(vec);
    return 0;
}
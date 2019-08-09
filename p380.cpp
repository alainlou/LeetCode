#include <bits/stdc++.h>

using namespace std;

class RandomizedSet {
private:
    unordered_set<int> data;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(data.find(val) != data.end())
            return false;
        data.insert(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        auto iter = data.find(val);
        if(iter != data.end()) {
            data.erase(iter);
            return true;
        } else {
            return false;
        }
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        auto random_iter = next(begin(data), rand()%data.size());
        return *random_iter;
    }
};

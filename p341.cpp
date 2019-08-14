#include <bits/stdc++.h>

using namespace std;

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
public:
    int curr = 0;
    vector<int> list;
    
    void unpack(vector<NestedInteger> &nestedList) {
        for(NestedInteger n : nestedList) {
            if(n.isInteger())
                list.push_back(n.getInteger());
            else
                unpack(n.getList());
        }        
    }
    
    NestedIterator(vector<NestedInteger> &nestedList) {
        unpack(nestedList);
    }

    int next() {
        return list[curr++];
    }

    bool hasNext() {
        return curr < list.size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
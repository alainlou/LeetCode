#include <bits/stdc++.h>

using namespace std;

struct DoublyLinkedNode {
    int key;
    int val;
    DoublyLinkedNode* next;
    DoublyLinkedNode* prev;
    DoublyLinkedNode(int k, int v) : key(k), val(v), next(NULL), prev(NULL) { }
};

class LRUCache {
public:
    int cap;
    int size;
    unordered_map<int, DoublyLinkedNode*> dictionary;
    DoublyLinkedNode* head;
    DoublyLinkedNode* tail;
    
    LRUCache(int capacity) {
        cap = capacity;
        size = 0;
        head = NULL;
        tail = NULL;
    }
    
    void make_head(int key) {        
        // if it's already the head, do nothing
        if(head == dictionary[key])
            return;
        
        // update tail
        if(tail == dictionary[key]) {
            tail = tail -> prev;
        }
        
        // make the ones beside point to the right place
        DoublyLinkedNode* right = dictionary[key]->next;
        DoublyLinkedNode* left = dictionary[key]->prev;
        if(left != NULL)
            left->next = right;
        if(right != NULL)
            right->prev = left;
        
        // actually make it the head
        dictionary[key]->prev = NULL;        
        head->prev = dictionary[key];
        dictionary[key]->next = head;
        head = dictionary[key];
    }
    
    void set_head(int key, int value) {
        DoublyLinkedNode* front = new DoublyLinkedNode(key, value);
        front->next = head;
        head->prev = front;
        head = front;
    }
    
    int get(int key) {
        // not found
        if(dictionary.find(key) == dictionary.end())
            return -1;
        // get the value
        int value = dictionary[key]->val;
        // do nothing
        if(cap == 1) {
            return value;
        }
        make_head(key);
        return value;        
    }
    
    void put(int key, int value) {
        ++size;
        // set the value
        if(dictionary.find(key) != dictionary.end()) {
            --size;
            dictionary[key]->val = value;
            // we need to move it to head as well
            make_head(key);
        } 
        // over capacity - evict and add
        else if(size > cap) {
            // evict last one
            // case that cap is 1
            if(cap == 1) {
                dictionary.erase(tail->key);
                head = new DoublyLinkedNode(key, value);
                tail = head;            
            } else {
                dictionary.erase(tail->key);
                tail = tail->prev;
                tail->next = NULL;
                delete tail->next;
                set_head(key, value);
            }            
        }
        // still in capacity - just add
        else {
            // add to the head
            if(head == NULL) {
                head = new DoublyLinkedNode(key, value);
                tail = head;
                head->next = NULL;
            } else {
                set_head(key, value);
            }
        }
        dictionary[key] = head;
    }
};

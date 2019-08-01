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
    
    void printList() {
        DoublyLinkedNode* curr = head;
        while(curr != NULL) {
            cout << "{" << curr->prev << "," << "<" << curr->key << "," << curr->val <<">" << "," << curr->next << "} ";
            curr = curr->next;
        }
        cout <<endl;
    }
    
    void make_head(int key) {        
        // if it's already the head, do nothing
        if(head == dictionary[key])
            return;
        // put as most recent
        DoublyLinkedNode* right = dictionary[key]->next;
        DoublyLinkedNode* left = dictionary[key]->prev;
        if(left != NULL)
            left->next = right;
        if(right != NULL)
            right->prev = left;
        dictionary[key]->prev = NULL;
        if(size > 1) {
            head->prev = dictionary[key];
            dictionary[key]->next = head;
            head = dictionary[key];
        }
        
        // setting the appropriate tail - lazy
        DoublyLinkedNode* curr = head;
        while(curr->next) {
            curr = curr->next;
        }
        tail = curr;
    }
    
    int get(int key) {
        cout << "get " << key << endl;
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
        cout << "put " << key << " " << value << endl;
        ++size;
        // set the value
        if(dictionary.find(key) != dictionary.end()) {
            --size;
            dictionary[key]->val = value;
            // we need to move it to head as well
            make_head(key);
        } else if(size > cap) {
            // evict last one
            // case that cap is 1
            if(cap == 1) {
                dictionary.clear();
                head = new DoublyLinkedNode(key, value);
                tail = head;            
            } else {
                cout << "here";
                dictionary.erase(tail->key);
                tail = tail->prev;
                tail->next = NULL;
                delete tail->next;
                DoublyLinkedNode* tmp = new DoublyLinkedNode(key, value);
                tmp->next = head;
                head->prev = tmp;
                head = tmp;
            }            
        } else {
            // add to the head
            if(head == NULL) {
                head = new DoublyLinkedNode(key, value);
                tail = head;
                head->next = NULL;
            } else {
                DoublyLinkedNode* tmp = new DoublyLinkedNode(key, value);
                tmp->next = head;
                head->prev = tmp;
                head = tmp;
            }
        }
        dictionary[key] = head;
    }
};
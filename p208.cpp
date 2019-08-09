#include <bits/stdc++.h>

using namespace std;

class TrieNode {    
public:
    bool is_end;
    TrieNode* children[26];
    
    TrieNode() {
        for(int i = 0; i < 26; ++ i) {
            children[i] = NULL;
        }
        is_end = false;
    }
};

class Trie {
private:
    TrieNode* head;
public:
    /** Initialize your data structure here. */
    Trie() {
        head  = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* curr = head;
        for(char c : word) {
            if(curr->children[c-'a'] == NULL)
                curr->children[c-'a'] = new TrieNode();
            curr = curr->children[c-'a'];
        }
        curr->is_end = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* curr = head;
        for(char c : word) {
            if(curr->children[c-'a'] == NULL) {
                return false;
            }
            curr = curr->children[c-'a'];
        }
        return curr->is_end;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* curr = head;
        for(char c : prefix) {
            if(curr->children[c-'a'] == NULL) {
                return false;
            }
            curr = curr->children[c-'a'];
        }
        return true;
    }
};

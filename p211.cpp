#include <bits/stdc++.h>

using namespace std;

class TrieNode {
public:
    TrieNode* children[26];
    bool is_end;
    
    TrieNode() {
        for(int i = 0; i < 26; ++i) {
            children[i] = NULL;
        }
        is_end = false;
    }
};

class WordDictionary {
private:
    TrieNode* head;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        head = new TrieNode();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        TrieNode* curr = head;
        for(char c : word) {
            if(curr->children[c-'a'] == NULL) {
                curr->children[c-'a'] = new TrieNode();
            }
            curr = curr->children[c-'a'];
        }
        curr->is_end = true;
    }
    
    bool full(string word) {
        TrieNode* curr = head;
        for(char c : word) {
            if(curr->children[c-'a'] == NULL) {
                return false;
            }
            curr = curr->children[c-'a'];
        }
        return curr->is_end;
    }
    
    bool special(TrieNode* start, string word, int index) {    
        TrieNode* curr = start;
        for(int i = index; i < word.size(); ++i) {
            char c = word[i];
            if(c == '.') {
                if(i == word.size()-1) {
                    for(int k = 0; k < 26; ++k) {
                        if(curr->children[k] != NULL && curr->children[k]->is_end)
                            return true;
                    }
                    return false;
                }
                for(int j = 0; j < 26; ++j) {
                    if(curr->children[j] != NULL && special(curr->children[j], word, i+1))
                        return true;
                }
                return false;
            } else if(curr->children[c-'a'] == NULL) {
                return false;
            }
            curr = curr->children[c-'a'];       
        }
        return curr->is_end;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        if(count(word.begin(), word.end(), '.') == 0) {
            return full(word);
        }
        return special(head, word, 0);
    }
    
};

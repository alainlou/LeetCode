#include <bits/stdc++.h>

using namespace std;

struct TrieNode {
    bool end;
    TrieNode *children[26];
    
    TrieNode() {
        end = false;
        for(int i = 0; i < 26; ++i) {
            children[i] = NULL;
        }
    }
};

struct Trie {
    TrieNode *root;
    
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string s) {
        TrieNode *p_crawl = root;
        for(int i = 0; i < s.size(); ++i) {
            int index = s[i] - 'a';
            if(p_crawl->children[index] == NULL)
                p_crawl->children[index] = new TrieNode();
            p_crawl = p_crawl->children[index];
        }
        p_crawl->end = true;
    }
    
    bool search(string s) {
        TrieNode *p_crawl = root;
        for(int i = 0; i < s.size(); ++i) {
            int index = s[i] - 'a';
            if(p_crawl->children[index] == NULL)
                return false;
            p_crawl = p_crawl->children[index];
        }
        return (p_crawl != NULL && p_crawl->end);
    }
};

class Solution {
public:
    unordered_map<int, bool> results;
    Trie *t;
    bool process(string& s, int start) {
        if(start == s.size())
            return true;
        else if(results.find(start) != results.end())
            return false;
        // recursion
        for(int i = 1; i <= s.size() - start; ++i) {
            if(t->search(s.substr(start, i))) {
                bool result = process(s, start + i);
                if(result)
                    return true;
            }
        }
        results[start] = false;
        return false;
    }
    bool wordBreak(string s, vector<string>& wordDict) {
        t = new Trie();
        for(string s : wordDict) {
            t->insert(s);
        }
        return process(s, 0);
    }
};
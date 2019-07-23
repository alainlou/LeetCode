#include <bits/stdc++.h>

using namespace std;

struct TrieNode {
    bool end;
    TrieNode *children[26];

    TrieNode() {
        end = false;
        for(int i = 0; i < 26; ++i) {
            children[0] = NULL;
        }
    }
};

struct Trie {
    TrieNode *root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string str) {
        TrieNode *p_crawl = root;
        for(int i = 0; i < str.size(); ++i) {
            int index = str[i] - 'a';
            if(p_crawl->children[index] == NULL)
                p_crawl->children[index] = new TrieNode();
            p_crawl = p_crawl->children[index];
        }
        p_crawl->end = true;
    }

    bool search(string str) {
        TrieNode *p_crawl = root;
        for(int i = 0; i < str.size(); ++i) {
            int index = str[i] - 'a';
            if(p_crawl->children[index] == NULL)
                return false;
            p_crawl = p_crawl->children[index];
        }
        return p_crawl != NULL && p_crawl->end;
    }
};
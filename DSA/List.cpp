#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode * next;
    ListNode(int i) {
        val = i;
        next = NULL;
    }
};

struct LinkedList {
    ListNode * head;
    LinkedList(int i) {
        head = new ListNode(i);
    }
    void insert(int i) {
        if(head == NULL)
            head = new ListNode(i);
        ListNode * curr = head;
        while(curr->next) {
            curr = curr->next;
        }
        curr->next = new ListNode(i);
    }
    void print() {
        ListNode * curr = head;
        while(curr) {
            cout << curr->val << " ";
            curr = curr->next;
        }
        cout << endl;
    }
    void reverse() {
        ListNode * prev = NULL;
        ListNode * curr = head;
        ListNode * next;
        while(curr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
    }
};

int main() {
    LinkedList list = LinkedList(0);
    list.insert(1);
    list.insert(2);
    list.insert(3);
    list.insert(4);
    list.insert(5);
    list.insert(6);
    list.insert(7);
    list.insert(8);
    list.print();
    list.reverse();
    list.print();
    return 0;
}
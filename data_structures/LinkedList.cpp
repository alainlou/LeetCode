#include <cstddef>
#include <iostream>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int i) : val(i), next(NULL) { }
};

struct LinkedList {
    ListNode* head;
    LinkedList(int i) : head(new ListNode(i)) { }
    void insert(int i) {
        ListNode* curr = head;
        while(curr->next) {
            curr = curr->next;
        }
        curr->next = new ListNode(i);
    }
    void reverse() {
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next;
        while(curr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
    }
    void print() {
        ListNode* curr = head;
        while(curr) {
            std::cout << curr->val << " -> ";
            curr = curr->next;
        }
        std::cout << "END" << std::endl;
    }
};

int main () {
    // Instantiate a LinkedList
    LinkedList* list = new LinkedList(1);

    // Insert some nodes
    list->insert(2);
    list->insert(3);
    list->insert(4);

    // Print the LinkedList
    list->print();

    // Reverse the LinkedList
    list->reverse();

    // Print the LinkedList to check the reverse worked
    list->print();
    return 0;
}

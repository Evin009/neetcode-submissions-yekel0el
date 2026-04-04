/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;
        ListNode* first = head;
        ListNode* toDelete = nullptr;
        int len = 1;
        

        if (head == nullptr) return NULL;

        while (temp != NULL && temp->next != NULL){
            len++;
            temp = temp->next;
        }

        int idx = len - n;
        if (idx == 0){
            ListNode* newHead = head->next;
            delete head;
            return newHead;
        }

        for (int i = 1; i < idx; i++){
            first = first->next;
        }

        toDelete = first->next;
        first->next = toDelete->next;
        delete toDelete;
        return head;
        
        
    }
};

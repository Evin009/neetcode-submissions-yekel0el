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
    void reorderList(ListNode* head) {
    
        ListNode* fast = head;
        ListNode* slow = head;


        while (fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* second = slow->next;
        ListNode* prev = slow->next = nullptr;
        while (second != nullptr){
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        ListNode* tempHead = head;
        second = prev;
        while (second != nullptr){
            ListNode* tmp1 = tempHead->next;
            ListNode* tmp2 = second->next;
            tempHead->next = second;
            second->next = tmp1;
            tempHead = tmp1;
            second = tmp2;
        }



        // while (slow != NULL){
        //     st.push(slow);
        //     slow = slow->next;
        // }

        // while (head){
        //     tail->next = head;
        //     head = head->next;
        //     head->next = st.top();
        // }
        // tail = tail->next;
        

        



        // ListNode* tailList = head;
        // while (tailList->next != NULL && tailList != NULL){
        //     tailList = tailList->next;
        // }

        // if (head == NULL) return;

        // while (!head){
        //     tail->next = head;
        //     head = head->next;
        //     tail = tail->next;
        //     tail->next = tailList;
        // }

        


    }
};

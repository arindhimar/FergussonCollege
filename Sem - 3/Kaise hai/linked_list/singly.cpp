#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node *next;

    Node(int val){
        this->data = val;
        this->next = nullptr;
    }
};

void menu(){
    cout << "1 - Insert\n";
    cout << "2 - Delete\n";
    cout << "3 - Display\n";
    cout << "4 - Exit\n";
}

Node* add(Node *head){
    int val;
    cout << "Enter value: ";
    cin >> val;
    Node *newNode = new Node(val);
    if (head == nullptr) {
        head = newNode;
    } else {
        Node *temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    return head;
}

void display(Node *head){
    if (head == nullptr) {
        cout << "List is empty.\n";
        return;
    }
    Node *temp = head;
    cout << "Data: ";
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

Node* deleteNode(Node *head){
    int pos;
    cout << "Enter position to delete: ";
    cin >> pos;

    if (head == nullptr) {
        cout << "List is empty.\n";
        return head;
    }

    if (pos == 1) {
        Node *temp = head;
        head = head->next;
        delete temp;
        return head;
    }

    Node *temp = head;
    int count = 1;

    while (temp != nullptr) {
        count++;
        if (count == pos) {
            if (temp->next == nullptr) { 
                Node *prev = head;
                while (prev->next != temp) {
                    prev = prev->next;
                }
                prev->next = nullptr;
                delete temp;
                return head;
            } else {
                temp->data = temp->next->data;
                temp->next = temp->next->next;
                return head;
            }
        }
        temp = temp->next;
    }

    cout << "Invalid position.\n";
    return head;
}

int main() {
    int opt = 0;
    Node *head = nullptr;
    
    do {
        menu();
        cout << "Select an option: ";
        cin >> opt;

        switch(opt){
            case 1:
                head = add(head);
                break;
            case 2:
                head = deleteNode(head);
                break;
            case 3:
                display(head);
                break;
            case 4:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid option.\n";
        }

    } while(opt != 4);

    return 0;
}

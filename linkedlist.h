#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include <iostream>
using namespace std;


class LinkedList {

  private:
    struct Node{
      int value;
      Node *next;
    };

    Node * head;
  public:
    LinkedList();
    void appendNode(int);
    void insertNode(int);
    void deleteNode(int);
    void displayList() const;
};

#endif
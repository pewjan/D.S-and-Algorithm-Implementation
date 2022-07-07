#include "linkedlist.h"
#include <iostream>
using namespace std;


LinkedList::LinkedList(){
  head = nullptr;
}



void LinkedList::appendNode(int num){
  Node * newNode = new Node;
  Node * nodePtr;
  newNode->value = num;
  newNode->next = nullptr;
  if(head == NULL){
    head = newNode;
  }else{
    nodePtr = head;

    while(nodePtr->next != NULL){
      nodePtr = nodePtr->next;
    }
    nodePtr->next = newNode;
  }
  
}
void  LinkedList::insertNode(int num){
  Node * newNode = new Node;
  Node * nodePtr;
  Node * prevNode = nullptr;

  newNode->value = num;
  newNode->next = NULL;
  if(head == NULL){
    head = newNode;
  }else{
    nodePtr = head;
    while(nodePtr != NULL && nodePtr->value < num){
      prevNode = nodePtr;
      nodePtr = nodePtr->next;
    }
    if(prevNode == nullptr){
      head = newNode;
      newNode->next = nodePtr;
    }else{
      prevNode->next = newNode;
      newNode->next = nodePtr;
    }
  }
  
}
void  LinkedList::deleteNode(int num){
  Node * nodePtr = head;
  Node * prevNode = head;

  if(head == NULL){
    return;
  }
  if(head->value == num){
    head = nodePtr->next;
    delete nodePtr;
    nodePtr = head;
  }else{
    while(nodePtr != nullptr && nodePtr->value != num){
      prevNode = nodePtr;
      nodePtr = nodePtr->next;
    }
    if(nodePtr != nullptr){
      prevNode->next = nodePtr->next;
      delete nodePtr;
    }
  }
  
}
void  LinkedList::displayList() const{

  Node * nodePtr;
  nodePtr = head;
  if(head == NULL){
    cout << "The LinkedList is empty!" << endl;
  } else {
    while(nodePtr != NULL){
      cout << nodePtr->value << " ";
      nodePtr = nodePtr->next;
    }
    cout << endl;
    return;
  }
  
}

#include <iostream>
#include "Queue.h"

using namespace std;


Queue::Queue(){
}
void Queue::Enqueue(int x){
  Node * newNode = new Node;
  newNode->value = x;
  newNode->next = nullptr;
  if(frontPtr == NULL && rearPtr == NULL){
    frontPtr = newNode;
    rearPtr = newNode;
  }else{
    rearPtr->next = newNode;
    rearPtr = newNode;
    
  }
}
void Queue::Dequeue(){
  Node * nodePtr;
  nodePtr = frontPtr;
  if(frontPtr == NULL){
    return;
  }else if(frontPtr == NULL && rearPtr == NULL){
    frontPtr = rearPtr = NULL;
  }
  frontPtr = frontPtr->next;
  delete nodePtr;
  
  
}
void Queue::front(){
  cout << frontPtr->value << endl;
  return;
}
void Queue::rear(){
  cout << rearPtr->value << endl;
}
void Queue::IsEmpty(){
  if(frontPtr == NULL && rearPtr == NULL){
    cout << "True" << endl;
  }
  else{cout << "False" << endl;
    }
  return;
  
}
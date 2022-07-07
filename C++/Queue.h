#ifndef QUEUE_H
#define QUEUE_H

class Queue{
private:
  struct Node{
    int value;
    Node * next;
  };
  Node * frontPtr = nullptr;
  Node * rearPtr = nullptr;;


public:
  Queue();
  void Enqueue(int x);
  void Dequeue();
  void front();
  void rear();
  void IsEmpty();

};

#endif
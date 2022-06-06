#ifndef STACK_H
#define STACK_H

class Stack{

private:
  int SIZE = 0;
  int * StackArr = new int[SIZE];
  int top = -1;

public:
  Stack();
  Stack(int);
  void push(int);
  void pop();
  void displayStack() const;
};





#endif
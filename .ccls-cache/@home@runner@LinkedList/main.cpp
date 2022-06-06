#include <iostream>
#include "linkedlist.h"
#include "Stack.h"


using namespace std;


int main(){
  Stack stack;
  stack.push(2);
  stack.push(5);
  stack.push(10);
  stack.displayStack();
  stack.pop();
  cout << endl;
  stack.displayStack();
  stack.pop();
  stack.pop();
  stack.displayStack();
  cout << endl;
  stack.pop();
  stack.push(2);
  stack.push(5);
  stack.push(10);
  stack.push(11);
  stack.push(12);
  stack.displayStack();
  cout << endl;
  stack.push(38);
  cout << endl;
  stack.displayStack();
  
  
  
  
  
  
}
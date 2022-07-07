#include <iostream>
#include "Stack.h"

using namespace std;



Stack::Stack(int x){
  SIZE = x;
}
Stack::Stack(){
  SIZE = 5;
}

void Stack::push(int x){
  if(top == SIZE - 1){
    cout << "StackOverFlow" << endl;
    return;
  }
  top++;
  StackArr[top] = x;
  
}
void Stack::pop(){
  if(top == -1){
    cout << "No Element To POP" <<endl;
    return;
  }
  top--;
  
}

void Stack::displayStack() const{
  int i = top;
  while(i != -1){
    cout << StackArr[i] << endl;
    i--;
  }
  return;
  
}
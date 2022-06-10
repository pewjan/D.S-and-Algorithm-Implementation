#include <iostream>
#include "linkedlist.h"
#include "Stack.h"
#include "Queue.h"
#include "BinaryTree.h"

using namespace std;



int main(){
  int TreeValues[10] = {50,70,10,5,13,15,9,8,4,11};
  BinaryTree tree;


  tree.InOrderTraversal();
  for(int i = 0; i < 10; i++){
    tree.Add(TreeValues[i]);
  }

  
}
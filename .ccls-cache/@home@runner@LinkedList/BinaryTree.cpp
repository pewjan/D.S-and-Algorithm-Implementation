#include <iostream>
#include "BinaryTree.h"

using namespace std;



BinaryTree::BinaryTree(){
  rootNode = nullptr;
  
}
void BinaryTree::Add(int x){
  insert(rootNode, x);
  
  
}
BinaryTree::BinaryNode * BinaryTree::insert(BinaryNode  * rootNode, int x){
  BinaryNode * newNode = new BinaryNode;
  newNode->value = x;
  BinaryNode * nodePtr;
  if(rootNode == NULL){
    rootNode = newNode;
    return rootNode;
  }else if(x <= rootNode->value){
      rootNode->leftNode = insert(rootNode->leftNode, x);
  }else{
    rootNode->rightNode = insert(rootNode->rightNode, x);
  }
  return rootNode;
  
  
  
}
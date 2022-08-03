#include <iostream>
#include "BinaryTree.h"

using namespace std;



BinaryTree::BinaryTree(){
  rootNode = nullptr;
  
}
void BinaryTree::Add(int x){
  insert(rootNode, x);
  
  
}

void  BinaryTree::insert(BinaryNode  * nodePtr, int x){
  BinaryNode * newNode = new BinaryNode;
  newNode->value = x;

  if(rootNode == nullptr){
    rootNode = newNode;
    return;
  }
  if(nodePtr->value > x){
    if(nodePtr->leftNode != nullptr){
      insert(nodePtr->leftNode, x);
    }else{
      nodePtr->leftNode = newNode;
    }
    
  }else if(nodePtr->value < x){
    if(nodePtr->rightNode != nullptr){
      insert(nodePtr->rightNode, x);
    }else{
      nodePtr->rightNode = newNode;

      
    }
  }else{
    cout << "That number has already been added?!?!?!" << endl;
  }

  
  
}

  void BinaryTree::InOrderTraversal(){
    BinaryTree::find(rootNode);
  }

  void BinaryTree::find(BinaryNode  * nodePtr){
    if(rootNode != nullptr){
      if(nodePtr->leftNode != nullptr){
        BinaryTree::find(nodePtr->leftNode);
      }
      cout << nodePtr->value << " ";
      if(nodePtr->rightNode != nullptr){
        BinaryTree::find(nodePtr->rightNode);
    }
  }
    else{
        cout << "Empty Tree" << endl;
        
    }
  }
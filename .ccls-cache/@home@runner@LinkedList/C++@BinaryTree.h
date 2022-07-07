#ifndef BINARYTREE_H
#define BINARYTREE_H

class BinaryTree{

private:
  struct BinaryNode{
    int value;
    BinaryNode * leftNode;
    BinaryNode * rightNode;
  };

  BinaryNode * rootNode;
  void insert(BinaryNode  * nodePtr, int x);
  void find(BinaryNode  * nodePtr);
  
  //BinaryTree::BinaryNode * deleteNode(BinaryNode * rootNode, int x);
public:
  BinaryTree();
  void Search(int);
  void Add(int);
  void InOrderTraversal();
  




};




#endif
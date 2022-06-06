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
  BinaryTree::BinaryNode * insert(BinaryNode  * rootNode, int x);
public:
  BinaryTree();
  void Search(int);
  void Add(int);
  
  void Remove(int);




};




#endif
#ifndef HASHTABLE_H
#define HASHTABLE_H
#include <iostream>

using namespace std;


class HashTable{

private:
  static const int tableSize = 10;


  struct Node{
    string name = "empty";
    string drink = "empty";
    Node * next = nullptr;
  };


  Node * HashTableArray[tableSize];





public:
  HashTable();
  int Hash(string key);
  void addItem(string name, string drink);

};






#endif

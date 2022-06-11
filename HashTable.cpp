#include <iostream>
#include "HashTable.h"

using namespace std;


HashTable::HashTable(){
  for(int i = 0; i < tableSize; i++){
    HashTableArray[i] = new Node;
  }

  
  
}
int HashTable::Hash(string key){  
  int hash = 0;
  int index;


  for(int i = 0; i < key.length(); i++){
    hash = hash + (int)key[i]; 
  }

  index = hash % tableSize;

  return index;

  
}

void HashTable::addItem(string name, string drink){

  int index = Hash(name);
  if(HashTableArray[index]->name == "empty"){
    HashTableArray[index]->name = name;
    HashTableArray[index]->drink = drink;
    
  }else{
    Node * nodePtr = HashTableArray[index];
    Node * newNode = new Node;
    newNode->name = name;
    newNode->drink = drink;
    newNode->next = nullptr;
    while(nodePtr->next != nullptr){
      nodePtr = nodePtr->next;
    }
    nodePtr->next = newNode;
    
  }
  
}
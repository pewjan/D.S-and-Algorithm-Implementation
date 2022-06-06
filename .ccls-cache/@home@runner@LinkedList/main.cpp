#include <iostream>
#include "linkedlist.h"


using namespace std;


int main(){
  LinkedList list;
  list.appendNode(10);
  list.appendNode(20);
  list.appendNode(30);
  list.displayList();

  list.deleteNode(30);
  list.displayList();
  list.insertNode(100);
  list.displayList();
  
}
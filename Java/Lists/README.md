## Lists

### List Objects
These are examples of the List obejct types:
- Array
- Vectors
- Singly/Doubly Linked List

These are the common methods found in List objects
- add
- remove
- get
- contains
- indexOf
- isEmpty
- size

### Abstract Data Type
- Doesn't dictate how the data is organized
- Dictates the operations you can perform
- Concrete data structure is usually a concrete class
- Abstract data type is usually an interface

### ArrayList
Unlike an Array, ArrayList is a resizable array implementation of the List interface. If don't we specify the initialCapacity, by default it would have initialCapcity of 10.
- Capacity is the maximum number of items that could be stored before it needs to be resized.
- Size is the current number of items.
- Accessing an element at an index would have time complexity of O(1).
- However, adding or removing an element to and from an ArrayList may require 
  resizing and shifting elements, thus have time complexity of O(n).

### LinkedList
- Each item in the list is called a node.
- Each node has an item and a pointer to another node.
- For a Singly Linked List, there is only one pointer to the next node.
- For a Doubly Linked List, there are two pointers: one to previous and another to the next node.
- The first item in the list is the head of the list.
- The last item in the list is the tail of the list. The last node will always point to null.
- Insert will have O(1) time complexity as we simply make the head pointer to the new node.
- Likewise, Remove will also have O(1) time complexity as it's a simple pointer reassignment.


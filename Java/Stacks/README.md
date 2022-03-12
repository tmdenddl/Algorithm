## Stacks

### Stack
- Abstract data type
- Follows LIFO principle - Last In First Out. Think of a stack of dishes.
- Has the following methods:
  - push: adds an item as the top item on the stack
  - pop: removes the top item on the stack
  - peek: gets the top item on the stack without popping(removing) it
- Ideal backing data structure would be a linked list

### Time Complexity
- O(1) for push, pop, and peek, when using a LinkedList
- If you use an array, then push is O(n) because the array may have to be resized.
- If you know the maximum number of items that will ever be on the stack, an array can be a good choice.
- If memory is tight, an array might be a good choice.
- Linked List is ideal on most of other cases.
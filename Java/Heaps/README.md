## Heaps

### Heap
- A complete binary tree
- Must satisfy the heap property:
  - Max heap: Every parent is greater than or equal to its children
  - Min heap: Every parent is less than or equal to its children

### Binary Heap
- Must be a complete tree
- Children are added at each level from left to right
- Usually implemented as arrays
- The maximum or minimum value will always be at the root of the tree - the advantage of using a heap
- Heapify: process of converting a binary tree into a heap
  - This often has to be done after an insertion or deletion
- No required ordering between the siblings

### Heaps as Arrays
- We can store binary heaps as arrays
- We put the root at array[0]
- We then traverse each level from left to right:
  - Left child of the root would go into array[1]
  - Right child of the root would go into array[2]

### Example:
            22
           /   \
          19    18
         /  \   / \
        15  3  14  4
       / \
      12

Array: [22, 19, 18, 15, 3, 14, 4, 12]

For the node at array[i]:
- Left child = 2i + 1
- Right child = 2i + 2
- Parent = floor((i - 1) / 2)

### Insert into Heap
- Always add new items to the end of the array
- Then we have to fix the heap (heapify)
- We compare the new item against its parent
- If the item is greater than its parent, we swap it with its parent
- We then rinse and repeat
- Use the equations above to get the parent index

### Delete from Heap
- Must choose a replacement value
- Will take the rightmost value, so that the tree remains complete
- Then we must heapify the heap
- When the replacement value is greater than the parent, fix heap above.
  Otherwise, fix heap below
- Fix heap above - same as insert. Swap replacement value with parent
- Fix heap below - swap the replacement value with the larger of its two children
- Rinse and repeat in both cases until the replacement value is in its correct position
- Will only need to fix up or down, not both

### PriorityQueue
- Max Heap is used to implement Priority Queue
- The value with the highest priority is always at the root of the heap
- When we want to remove the highest priority item, we simply remove the root
- Highest value means less priority. For example, 1 has the higher priority than 100
- Operations:
  - add | enqueue: add an element to the queue
  - peek: return the highest priority item, but do not remove it from the heap
  - poll | remove | dequeue: remove an element from the queue

### HeapSort
- We know the root has the largest value
- Swap root with the last element in the array
- Heapify the tree, but exclude the last node
- After heapify, second largest element is at the root
- Rinse and repeat

1. Swap the root with the last element in the array. The root is now in the correct position.
2. Then we heapify the tree, excluding the last element which is already in the correct position.
   At this point, the new root will be the second largest element in the array.
3. Repeat the step 1 - 2 until every node has been placed into the correct position


## Sort Algorithms

### Stable & Unstable Sort
Stable sort will preserve the order of the same valued element during sort. 
However, unstable sort will not preserve the order.

For example: [5, 9-1, 3, 9-2, 8, 4]  
Note that we marked 9 as 9-1 and 9-2 to track the order.

Stable sort: [3, 4, 5, 8, 9-1, 9-2]
Unstable sort: [3, 4, 5, 8, 9-2, 9-1]

Sort algorithms can either be stable or unstable depending on the implementation method.

### Bubble Sort
Bubble sort's performance degrades as the number of elements in the array increases.
Bubble sort doesn't require any extra memory. 
It uses the array given to partition the array into two: sorted and unsorted parts.

Basically we have two indexes: u (unsorted) and s (sorted) index which initially starts at 0 and n.
1. Compare the element at u and u + 1.
2. Swap the elements if an element at u + 1 is smaller than the element at index u.
3. Increment u, then repeat the same procedure until u index equals s index.
    Then the element at index s will be sorted.
4. Repeat the steps 1 - 3, this time with u = 0 and s = n - 1.
    Repeat until u == s at the the start of the step.

Bubble Sort is an in-place algorithm, meaning it doesn't require any extra memory.
It's got O(n^2) time complexity - quadratic.

### Selection Sort
Selection sort is similar to the bubble sort in a sense that we have unsorted and sorted parts of an array.
However, this time we are traversing through an array to find the biggest element, then swap it with element at index s.
This will make any elements at index greater than index s sorted.

1. Traverse through an array, find the largest element in unsorted partition.
2. Swap with the element at index s. Then decrement s.
3. Repeat step 1 - 2 until every elements are sorted, meaning index u == s.

Selection Sort is an in-place algorithm.
It's got O(n^2) time complexity - quadratic. Selection Sort does not require as much swapping as Bubble Sort.

### Insertion Sort

Like Bubble Sort and Selection Sort, Insertion Sort also partitions the array into sorted and unsorted partitions.
However, this time we have the sorted partition in the beginning of the array, not the end.
By default at the very beginning, the first element is considered as sorted as it's the only element in the sorted partition.

We traverse the sorted partition from right to left - from largest to smallest.
If an element at index i in the sorted partition is less than or equal to the element we're trying to insert,
then all of the values to the left of element i will be less than or equal to the value we're trying to insert,
because all the values are in a sorted order.

1. Take the element at firstUnsortedIndex, compare it with the last element in the sorted partition.
2. If the new element is smaller than the current element in the sorted partition, keep swaping until finding 
    the correct position in the sorted partition. If the new element is greater than the current element, we don't swap)
3. Repeat step 1 - 2 until the firstUnsortedIndex equals the last element in the sorted partition.

Insertion Sort is also an in-place algorithm.
It's got O(n^2) time complexity - quadratic.
It's also a stable algorithm.


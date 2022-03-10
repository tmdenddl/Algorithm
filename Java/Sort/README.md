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

### Shell Sort
Shell Sort is a variation of the Insertion Sort.
Insertion sort chooses which element to insert using a gap of 1. 
However, Shell sort starts out using a larger gap value.
At every iterations, the array becomes more sorted. Then gap is decremented to reduce the amount of shifting required.

We'll base our gap on the array's length. We'll initialize the gap (or interval) to array.length/2.
On each iteration, we'll divide the gap value by 2 to get the next gap value, until reaching 1.

1. Compare the first element (newElement) with the element at 3 indexes away which is the initial value of the gap.
2. Swap if the newElement is bigger than the element we're comparing to.
3. Increment 
3. Then we go to the second element which becomes the newElement, then repeat what's done at step 1 - 2.
    Compare the elements at 3 indexes away.


Shell Sort is an in-place algorithm, meaning it doesn't require any extra memory.
It's got O(n^2) time complexity - quadratic.
It is an unstable algorithm.

### Merge Sort
Merge Sort is a Divide and Conquer algorithm. It uses recursive algorithm.
There are two phases: splitting and merging.
Splitting phase leads to a faster sorting during the Merging phase.
Merging phase basically merges the splitted arrays in a sorted manner.

Splitting is logical. We don't create new arrays. 
However, during Merging phase, we need temporary arrays.

Splitting Phase:
1. Start with an unsorted array.
2. Divide the array into two arrays, which are unsorted.
    The first array is the left array, and the second array is the right array.
3. Split the each left and right arrays into two arrays.
4. Keep splitting until all the arrays have only one element each - these arrays are sorted.

Merging Phase:
1. Merge every left/right pair of sibling arrays in a sorted manner into a sorted array.
    Note that we're copying into a temporary array. Travsering is done using index pointers on each array.
    Copy the smaller element to the temporary array, until both left/right arrays reach the end.
2. After the first merge, we'll have a bunch of 2-element sorted arrays.
3. Then merge those sorted arrays (left/right siblings) to end up with 
    a bunch of 4-element sorted arrays.
4. Repeat until you have a single sorted array.
5. Not in-place. Merging phase requires temporary arrays.

Although splitting phase is logical, since merging phase is not, Merge Sort is NOT an in-place algorithm.
It's got O(n*logn) time complexity. It's also a stable algorithm. 

### Quick Sort
Quick Sort is another Divide and Conquer algorithm. It also uses recursive algorithm like Merge Sort.
This time pivot element to partition the array into two parts is used.

1. Elements that are smaller than the pivot should be shifted to left of the pivot.
2. Likewise, elements that are larger than the pivot should be shifted to the right of the pivot.
    Note that at this moment, left and right sub-arrays are not necessarily sorted.
3. Pivot will then be shifted to its correct sorted position at the end.
4. Step 1 - 3 are now repeated for the left array and right array.
5. Eventually, every element has been the pivot, so every element will be in its correct sorted position.

As with Merge Sort, we'll end up partitioning the array into a series of 1-element arrays

Quick Sort uses logical parition, thus it's in-place algorithm.
It's got O(n*logn) time complexity. It's also an unstable algorithm. 

### Counting Sort
THIS IS TO BE DONE WHEN THE TIME IS ALLOWED

### Stable Counting Sort
THIS IS TO BE DONE WHEN THE TIME IS ALLOWED

### Radix Sort
THIS IS TO BE DONE WHEN THE TIME IS ALLOWED
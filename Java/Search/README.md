## Search

### Linear Search
- Data doesn't need to be sorted
- Traverse through an array or a list until you find the element you are looking for.
- Because of the traversal, the worst time complexity would be O(n) - Linear.

### Binary Search
- Data must be sorted.
- Chooses the element in the middle of the array and compares it against the search value.
- If element is equal to the value, we've found the element.
- If element is greater than the value, search the left half of the array.
- if element is less than the value, search the right half of the array.
- At some point, there will be only one element in the partition you're checking, but it doesn't have to get to that point.
- In each iteration, array size is divided into half, thus dramatically decreasing the time complexity.
- Can be implemented recursively
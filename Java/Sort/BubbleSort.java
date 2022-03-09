package Java.Sort;

public class BubbleSort {
    /*
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
    */

    // METHODS:

    // Swap elements at index i and index j within the given array
    public static void swap(int[] array, int i, int j) {
        if (i == j) {
            return;
        }

        int temp = array[i];
        array[i] = array[j]; 
        array[j] = temp;
    }

    public static void bubbleSort(int[] array) {
        // Repeat until sorted index becomes 0
        for (int s = array.length - 1; s > 0; s--) {
            // Traverse through the array reaching the sorted index
            for (int u = 0; u < s; u++) {
                // If array[u] > array[u + 1], swap the two elements
                if (array[u] > array[u + 1]) {
                    swap(array, u, u + 1);
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] intArray = {20, 35, -15, 7, 55, 1, -22};

        bubbleSort(intArray);

        for (int i = 0; i < intArray.length; i++) {
            System.out.println("intArray[i]: " + intArray[i]);
        }
    }
}

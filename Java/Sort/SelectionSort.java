package Java.Sort;

public class SelectionSort {
    /*
    Selection sort is similar to the bubble sort in a sense that we have unsorted and sorted parts of an array.
    However, this time we are traversing through an array to find the biggest element, then swap it with element at index s.
    This will make any elements at index greater than index s sorted.

    1. Traverse through an array, find the largest element in unsorted partition.
    2. Swap with the element at index s. Then decrement s.
    3. Repeat step 1 - 2 until every elements are sorted, meaning index u == s.

    Selection Sort is an in-place algorithm.
    It's got O(n^2) time complexity - quadratic. Selection Sort does not require as much swapping as Bubble Sort.
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

    public static void selectionSort(int[] array) {
        // Repeat until sorted index becomes 0
        for (int s = array.length - 1; s > 0; s--) {
            // index of the largest element of the unsorted partition.
            int largest = 0;

            // Traverse through the array reaching the sorted index
            for (int u = 1; u <= s; u++) {
                // Update the largest if
                if (array[u] > array[largest]) {
                    largest = u;
                }
                
            }

            // Swap the largest element of the unsorted partition with the element at index s which is not yet sorted.
            // Note only elements at index greater than index s will be sorted.
            swap(array, largest, s);
        }
    }

    public static void main(String[] args) {
        int[] intArray = {20, 35, -15, 7, 55, 1, -22};

        selectionSort(intArray);

        for (int i = 0; i < intArray.length; i++) {
            System.out.println("intArray[i]: " + intArray[i]);
        }
    }
}

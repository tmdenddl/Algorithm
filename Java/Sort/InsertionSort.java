package Java.Sort;

public class InsertionSort {
    /*
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

    public static void insertionSort(int[] array) {
        // We're iterating through the array from left to right until reaching the end
        for (int firstUnsortedIndex = 1; firstUnsortedIndex < array.length; firstUnsortedIndex++) {
            // Save the value of the first element at unsorted partition which is to be placed into sorted partition. 
            int newElement = array[firstUnsortedIndex];

            int i;
            // Traverse through unsorted partition starting from the first element until the first element's index becomes 0.
            // If insertion position is 0, the element is the smallest element in the sorted partition.
            // We want to keep traversing as long as the element we're trying to insert in the sorted partition is greater than
            // the one we currently have the pointer at (index i). If the element we have is greater than the element in the sorted partition,
            // we've found the correct index for the elemen in the sorted partition.
            // Basically we're traversing down the sorted partition - from the largest to the smallest, and 
            for (i = firstUnsortedIndex; i > 0 && array[i - 1] > newElement; i--) {
                array[i] = array[i - 1];
            }
            array[i] = newElement;
        }
    }

    public static void main(String[] args) {
        int[] intArray = {20, 35, -15, 7, 55, 1, -22};

        insertionSort(intArray);

        for (int i = 0; i < intArray.length; i++) {
            System.out.println("intArray[i]: " + intArray[i]);
        }
    }
}

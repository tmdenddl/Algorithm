package Java.Sort;

public class QuickSort {
    /*
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
    */

    // METHODS:
    public static void quickSort(int[] array, int start, int end) {
        // Base case: if we are left with one or zero element, break out of the recursive call
        if (end - start < 2) {
            return;
        }

        int pivotIndex = partition(array, start, end);

        // Handle left sub-arrays first, then the right sub-arrays.
        quickSort(array, start, pivotIndex);
        quickSort(array, pivotIndex + 1, end);
    }

    public static int partition(int[] array, int start, int end) {
        // This is using the first element as the pivot
        int pivot = array[start];
        int i = start;
        int j = end;

        // Since i increments and j decrements as we sorted around the pivot in each iteration,
        // we'll stop the iteration when the i and j meet
        while (i < j) {
            // Note: empty loop body
            // We'll break out of the while loop below if we've traversed through all the elements around pivot,
            // or if the element at array[j] is less than the pivot.
            while (i < j && array[--j] >= pivot);
            // Since we still haven't traversed through all the elements, continue...
            if (i < j) {
                // We've found the first element that's less than the pivot from the right sub-array,
                // so we want to move that towards the front of the array.
                array[i] = array[j];
            }

            // Note: empty loop body
            // We'll break out of the while loop below if we've traversed through all the elements around pivot,
            // or if the element at array[i] is larger than the pivot.
            while (i < j && array[++i] <= pivot);
            // Since we still haven't traversed through all the elements, continue...
            if (i < j) {
                // We've found the first element that's greater than the pivot from the left sub-array,
                // so we want to move that towards the back of the array.
                array[j] = array[i];
            }
        }
        // At this point, left of the pivot will be smaller than the pivot.
            // Likewise, right of the pivot will be larger than the pivot.
            // Thus, j would be an index where the pivot should be placed.
            array[j] = pivot;
            return j;
    }
    

    public static void main(String[] args) {
        int[] intArray = {20, 35, -15, 7, 55, 1, -22};

        quickSort(intArray, 0, intArray.length);

        for (int i = 0; i < intArray.length; i++) {
            System.out.println("intArray[i]: " + intArray[i]);
        }
    }
}

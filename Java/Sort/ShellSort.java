package Java.Sort;

public class ShellSort {
    /*
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
    */

    // METHODS:
    public static void shellSort(int[] array) {
        // For our array, the gap will be initialized to 3. On the next iteration, it will be 1 - Insertion Sort.
        // i = gap = 3
        // j = i - gap

        // Initial gap value should be array.length / 2, and at each iteration gap should be divided by 2
        for (int gap = array.length / 2; gap > 0; gap /= 2) {
            // Initial value of i is gap 
            for (int i = gap; i < array.length; i++) {
                int newElement = array[i];
                int j = i;

                // If j becomes smaller than the gap, we've hit the front of the array
                // If an element at array[j - gap] is greater than the element at array[j], swap the two elements
                while (j >= gap && array[j - gap] > newElement) {
                    array[j] = array[j - gap];
                    j -= gap;
                }

                // If array[j - gap] was greater than the element at array[j], we will be swapping elements at those indexes.
                // If not, nothing happens.
                array[j] = newElement;
            }
        }
        
    }

    public static void main(String[] args) {
        int[] intArray = {20, 35, -15, 7, 55, 1, -22};

        shellSort(intArray);

        for (int i = 0; i < intArray.length; i++) {
            System.out.println("intArray[i]: " + intArray[i]);
        }
    }
}

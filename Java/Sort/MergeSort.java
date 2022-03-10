package Java.Sort;

public class MergeSort {
    /*
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
    */

    // METHODS:
    public static void mergeSort(int[] array, int start, int end) {
        // start = 0
        // end = array.length
        // mid = (start + end) / 2

        // Base case: break recursion if there are less than 2 elements in the array - 1 or 0 elements
        if (end - start < 2) {
            return;
        }

        // Logical partition of the array
        int mid = (start + end) / 2;

        // Recursive calls
        mergeSort(array, start, mid);   // mergeSort left partition
        mergeSort(array, mid, end); // mergeSort right partition

        // Finally merge the sorted arrays. 
        // By the time this method is called, left and right partitions are already handled.
        merge(array, start, mid, end);
    }

    public static void merge(int[] array, int start, int mid, int end) {
        // If the last element of the left partition is smaller than or equal to the first element in the right partition,
        // that means all the elements in the left partition are smaller than the elements in the right partition.
        // This means they are already in a sorted manner, thus no work is needed to be done.
        if (array[mid - 1] <= array[mid]) {
            return;
        }

        // Index variables
        int i = start;
        int j = mid;
        int tempIndex = 0;

        // Create a temp array large enough to hold all elements in the left and right partitions
        int[] temp = new int[end - start];

        // While there are elements left in any of the left and right partitions...
        while (i < mid && j < end) {
            /* 
            temp[tempIndex++] = array[i] <= array[j] ? array[i++] : array[j++];
            */
            // If the left element is smaller than or equal to the right...
            if (array[i] <= array[j]) {
                // Assign the left element to the temp array, and increment tempIndex and i
                temp[tempIndex++] = array[i++];
            } else {
                // Else assign the right element to the temp array, and increment tempIndex and j
                temp[tempIndex++] = array[j++];
            }
        }

        // At this point, either left or right partition will now be empty. 
        // Then we simply merge the rest from another partition into temp array 
        // as elements left are all larger than the largest elements in the temp array.
        /*
        System.arraycopy(src, srcPos, dest, destPos, length)
        src => source array
        srcPos => source index
        dest => destination array
        destPos => destination index
        */

        // Start at unhandled index of the left partition and copy over the rest of the elements
        // to the end of the array from index we've copied over to temp array so far.
        // If there are left over elements in the right partitions, they're already in the end of the array.
        // In the next step, we will be copying over the sorted and merged array from temp array 
        // back to the original array, so the the beginning of the array is now sorted in the original array.
        System.arraycopy(array, i, array, start + tempIndex, mid - i);

        // Copy the elements in the temp array back into the original array
        System.arraycopy(temp, 0, array, start, tempIndex);
    }

    public static void main(String[] args) {
        int[] intArray = {20, 35, -15, 7, 55, 1, -22};

        mergeSort(intArray, 0, intArray.length);

        /*
        Splitting Phase (Arrows from Top to bottom):
                    {20, 35, -15, 7, 55, 1, -22}
                        /                   \
                {20, 35, -15}       {7, 55, 1, -22}
                    /   \               /       \
                {20}    {35, -15}   {7, 55}    {1, -22}
                        /   \        /   \       /   \
                      {35}  {-15}   {7}  {55}  {1}  {-22}


        Merging Phase (Arrows from bottom to top):
                    {-22, -15, 1, 7, 20, 35, 55}
                        /                   \
                {-15, 20, 35}       {-22, 1, 7, 55}
                    /   \               /       \
                {20}    {-15, 35}   {7, 55}    {-22, 1}
                        /   \        /   \       /   \
                      {35}  {-15}   {7}  {55}  {1}  {-22}
        */

        for (int i = 0; i < intArray.length; i++) {
            System.out.println("intArray[i]: " + intArray[i]);
        }
    }
}

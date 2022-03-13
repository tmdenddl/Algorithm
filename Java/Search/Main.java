package Java.Search;

public class Main {
    public static int linearSearch(int[] array, int value) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                return i;
            }
        }
        return -1;
    }

    public static int iterativeBinarySearch(int[] array, int value) {
        int start = 0;
        int end = array.length;

        while (start < end) {
            int mid = (start + end) / 2;
            if (array[mid] == value) {
                return mid;
            } else if (array[mid] < value) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return -1;
    }

    public static int recursiveBinarySearch(int[] array, int value) {
        return recursiveBinarySearch(array, 0, array.length, value);
    }

    public static int recursiveBinarySearch(int[] array, int start, int end, int value) {
        if (start >= end) {
            return -1;
        }

        int mid = (start + end) / 2;
        if (array[mid] == value) {
            return mid;
        } else if (array[mid] < value) {
            return recursiveBinarySearch(array, mid + 1, end, value);
        } else {
            return recursiveBinarySearch(array, start, mid, value);
        }
    }

    public static void main(String[] args) {
        int[] intArray = {20, 35, -15, 7, 55, 1, -22};
        int[] intSortedArray = {-22, -15, 1, 7, 20, 35, 55};

        /*
        * This section is for Linear Search: O(n) time complexity
        */
        System.out.println(linearSearch(intArray, -15));
        System.out.println(linearSearch(intArray, -5));

        /*
         * This section is for Iterative Binary Search: O(log n) time complexity
         */
        System.out.println(iterativeBinarySearch(intSortedArray, -15));
        System.out.println(iterativeBinarySearch(intSortedArray, -5));

        /*
         * This section is for Recursive Binary Search: O(log n) time complexity
         */
        System.out.println(recursiveBinarySearch(intSortedArray, -15));
        System.out.println(recursiveBinarySearch(intSortedArray, -5));
    }
}

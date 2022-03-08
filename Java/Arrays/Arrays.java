package Java.Arrays;

public class Arrays {
    public static void main(String[] args) {
        // Note: Arrays are not dynamic, so we must declare the size
        int[] intArray = new int[7];

        // intArray => [20, 35, -15, 7, 55, 1, -22]
        intArray[0] = 20;
        intArray[1] = 35;
        intArray[2] = -15;
        intArray[3] = 7;
        intArray[4] = 55;
        intArray[5] = 1;
        intArray[6] = -22;

        int index = -1;
        // Since we use for loop, in the worst case we would need to loop through the entire Array, 
        // thus the time comeplexity is O(n)
        for (int i = 0; i < intArray.length; i++) {
            System.out.println("intArray[i] : " + intArray[i]);
            if (intArray[i] == 7) {
                index = i;
                break;
            }
        }
        System.out.println("index : " + index);
    }
}
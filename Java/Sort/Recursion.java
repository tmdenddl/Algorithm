package Java.Sort;

public class Recursion {
    /*
    Factorial Algorithm (Iterative)
    1. If num == 0, the factorial is 1. Stop. We have the result, otherwise...
    2. Set factorial to 1.
    3. Set multiplier to 1.
    4. While multiplier != num, do steps 5 and 6.
    5. Multiply facotrial by multiplier and assign the result to factorial.
    6. Increment the multiplier by 1.
    7. Stop. The result is factorial.
    */

    /*
    Factorial Algorithm (Recursive)
    1! = 1 * 0!        = 1
    2! = 2 * 1         = 2 * 1!
    3! = 3 * 2 * 1     = 3 * 2!
    4! = 4 * 3 * 2 * 1 = 4 * 3!

    n! = n * (n - 1)!
    */

    public static int iterativeFactorial (int num) {
        // Step 1
        if (num == 0) {
            return 1;
        }

        // Step 2
        int factorial = 1;

        // Step 3 - 6
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }

        // Step 7
        return factorial;
    }

    /*
    recursiveFactorial(4)
    
    recursiveFactorial(4) = 4 * recursiveFactorial(3) = 4 * (3 * 2 * 1)
    recursiveFactorial(3) = 3 * recursiveFactorial(2) = 3 * (2 * 1)
    recursiveFactorial(2) = 2 * recursiveFactorial(1) = 2 * (1)
    recursiveFactorial(1) = 1
    */
    public static int recursiveFactorial (int num) {
        // Note that recursive calls require a base case, 
        // otherwise it would be stuck in infinite loop.
        if (num == 0) {
            return 1;
        }

        return num * recursiveFactorial(num - 1);
    }

    public static void main(String[] args) {
        System.out.println(iterativeFactorial(4));
        System.out.println(recursiveFactorial(4));
    }
    
}

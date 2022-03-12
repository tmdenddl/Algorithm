package Java.Queues;

import Java.Queues.Employee;
import Java.Queues.ArrayQueue;
import sun.misc.Queue;

public class Main {
    public static void main(String[] args) throws Exception {
        Employee janesJones = new Employee("Jane", "Jones", 123);
        Employee johnDoe = new Employee("John", "Doe", 4567);
        Employee marrySmith = new Employee("Mary", "Smith", 22);
        Employee mikeWilson = new Employee("Mike", "Wilson", 3245);
        Employee johnAdams = new Employee("John", "Adams", 4568);

        /*
         * This section is for Queue using Array implementation
         */
        ArrayQueue arrayQueue = new ArrayQueue(10);
        arrayQueue.add(janesJones);
        arrayQueue.add(johnDoe);
        arrayQueue.add(marrySmith);
        arrayQueue.add(mikeWilson);

        arrayQueue.printQueue();
        System.out.println("");

        System.out.println("Peek: " + arrayQueue.peek());
        System.out.println("");

        arrayQueue.remove();
        arrayQueue.add(johnAdams);

        arrayQueue.printQueue();
        System.out.println("");

        /*
         * This section is for Circular Queue using Array implementation
         */
        CircularQueue circularQueue = new CircularQueue(5);
        // circularQueue.add(janesJones);
        // circularQueue.add(johnDoe);
        // circularQueue.remove();
        // circularQueue.add(marrySmith);
        // circularQueue.remove();
        // circularQueue.add(mikeWilson);
        // circularQueue.remove();
        // circularQueue.add(johnAdams);

        circularQueue.add(janesJones);
        circularQueue.add(johnDoe);
        circularQueue.add(marrySmith);
        circularQueue.add(mikeWilson);
        circularQueue.add(johnAdams);

        circularQueue.printQueue();
        System.out.println("");

        System.out.println("Peek: " + circularQueue.peek());
        circularQueue.remove();
        circularQueue.remove();

        circularQueue.printQueue();
        System.out.println("");

        /*
         * This section is for Queue using LinkedList implementation
         */
        Queue queue = new Queue();
    }
}

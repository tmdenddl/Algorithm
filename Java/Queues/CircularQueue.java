package Java.Queues;

import Java.Queues.Employee;

public class CircularQueue {
    private Employee[] queue;
    private int front;
    private int back;

    public CircularQueue(int capacity) {
        queue = new Employee[capacity];
    }

    public void add(Employee employee) {
        // Example:
        // 0 - jane
        // 1 - john
        // 2 - mary - back
        // 3 - mike - front
        // 4 - bill

        // If the queue is full, and we want to resize it in the circular queue,
        // we would need to reset the array so the front goes to 0 index.

        // Example:
        // 0 - mike - front
        // 1 - bill
        // 2 - jane
        // 3 - john
        // 4 - mary - back
        // 5
        // ...
        // 9
        if (size() == queue.length - 1) {
            int numItems = size();
            Employee[] newArray = new Employee[2 * queue.length];

            // Copying from front of the queue to the end of the array
            System.arraycopy(queue, front, newArray, 0, queue.length - front);
            // Copying from start of the array to the back of the queue
            System.arraycopy(queue, 0, newArray, queue.length - front, back);

            queue = newArray;
            front = 0;
            back = numItems;
        }

        queue[back] = employee;
        if (back < queue.length - 1) {
            // Example:
            // 0 - jane - front
            // 1 - john
            // 2 - mary
            // 3 - mike
            // 4 - bill - back
            // 5
            // ...
            // 9
            back++;
        } else {
            // Example:
            // 0 -      - new back position...
            // 1
            // 2
            // 3 - mike - front
            // 4 - bill - back
            back = 0;
        }
    }

    public Employee remove() throws Exception {
        if (size() == 0) {
            throw new Exception();
        }

        Employee employee = queue[front];
        queue[front] = null;
        front++;

        if (size() == 0) {
            front = 0;
            back = 0;
        } else if (front == queue.length) {
            // If the front of the queue is at the end of the array,
            // and we need to remove the item, simply point front to the front of the array again.
            front = 0;
        }

        return employee;
    }

    public Employee peek() throws Exception {
        if (size() == 0) {
            throw new Exception();
        }

        return queue[front];
    }

    public int size() {
        if (front <= back) {
            return back - front;
        } else {
            return back - front + queue.length;
        }

    }

    public void printQueue() {
        if (front <= back) {
            for (int i = front; i < back; i++) {
                System.out.println(queue[i]);
            }
        } else {
            for (int i = front; i < queue.length; i++) {
                System.out.println(queue[i]);
            }
            for (int i = 0; i < back; i++) {
                System.out.println(queue[i]);
            }
        }

    }
}

package Java.Stacks;

import Java.Stacks.Employee;

public class Main {
    public static void main(String[] args) throws Exception {
        Employee janesJones = new Employee("Jane", "Jones", 123);
        Employee johnDoe = new Employee("John", "Doe", 4567);
        Employee marrySmith = new Employee("Mary", "Smith", 22);
        Employee mikeWilson = new Employee("Mike", "Wilson", 3245);
        Employee johnAdams = new Employee("John", "Adams", 4568);

        /*
        * This section is for Stack using Array implementation
        */
        ArrayStack arrayStack = new ArrayStack(10);

        arrayStack.push(janesJones);
        arrayStack.push(johnDoe);
        arrayStack.push(marrySmith);
        arrayStack.push(mikeWilson);
        arrayStack.push(johnAdams);

        arrayStack.printStack();

        System.out.println("Popped: " + arrayStack.pop());
        System.out.println(arrayStack.peek());
        System.out.println(arrayStack.peek());

        /*
         * This section is for Stack using LinkedList implementation
         */
        LinkedStack linkedStack = new LinkedStack();
        linkedStack.push(janesJones);
        linkedStack.push(johnDoe);
        linkedStack.push(marrySmith);
        linkedStack.push(mikeWilson);
        linkedStack.push(johnAdams);

        linkedStack.printStack();

        System.out.println("Popped: " + linkedStack.pop());
        System.out.println(linkedStack.peek());
        linkedStack.printStack();
    }
}

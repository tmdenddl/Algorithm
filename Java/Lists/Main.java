package Java.Lists;

import java.util.List;
import java.util.ArrayList;
import java.util.Vector;

public class Main {
    public static void main(String[] args) {
        Employee janesJones = new Employee("Jane", "Jones", 123);
        Employee johnDoe = new Employee("John", "Doe", 4567);
        Employee marrySmith = new Employee("Mary", "Smith", 22);
        Employee mikeWilson = new Employee("Mike", "Wilson", 3245);
        Employee johnAdams = new Employee("John", "Adams", 4568);

        /*
        * This section is for the ArrayList
        */
        List<Employee> employeeList = new ArrayList<>();
        // List<Employee> employeeList = new Vector<>();
        employeeList.add(janesJones);
        employeeList.add(johnDoe);
        employeeList.add(marrySmith);
        employeeList.add(mikeWilson);

        System.out.println("This is the ArrayList of the current Employees");
        employeeList.forEach(employee -> System.out.print(employee + ", "));
        System.out.println("");

        // System.out.println("employeeList.get(1): " + employeeList.get(1));
        // System.out.println("isEmpty: " + employeeList.isEmpty());
        // System.out.println("size: " + employeeList.size());
        // System.out.println(employeeList.contains(new Employee("Mary", "Smith", 22)));
        // System.out.println(employeeList.indexOf(new Employee("Mary", "Smith", 22)));

        employeeList.set(1, johnAdams);
        employeeList.add(3, johnDoe);
        employeeList.remove(2);

        System.out.println("This is the ArrayList of the current Employees");
        employeeList.forEach(employee -> System.out.print(employee + ", "));
        System.out.println("");

        System.out.println("This is the array of the current Employees");
        Employee[] employeeArray = employeeList.toArray(new Employee[employeeList.size()]);
        for (Employee employee: employeeArray) {
            System.out.print(employee + ", ");
        }
        System.out.println("");

        /*
         * This section is for the Singly LinkedList
         */
        System.out.println("This section is for the Singly LinkedList");
        EmployeeSinglyLinkedList singlyLinkedList = new EmployeeSinglyLinkedList();
        singlyLinkedList.addToFront(janesJones);
        singlyLinkedList.addToFront(johnDoe);
        singlyLinkedList.addToFront(marrySmith);
        singlyLinkedList.addToFront(mikeWilson);

        System.out.println("This is the Singly Linked List of the current Employee");
        singlyLinkedList.printList();

        singlyLinkedList.removeFromFront();
        System.out.println("This is the Singly Linked List of the current Employee");
        singlyLinkedList.printList();

        System.out.println("");

        /*
         * This section is for the Doubly LinkedList
         */
        System.out.println("This section is for the Doubly LinkedList");
        EmployeeDoublyLinkedList doublyLinkedList = new EmployeeDoublyLinkedList();
        doublyLinkedList.addToFront(janesJones);
        doublyLinkedList.addToFront(johnDoe);
        doublyLinkedList.addToFront(marrySmith);
        doublyLinkedList.addToFront(mikeWilson);

        System.out.println("This is the Doubly Linked List of the current Employee");
        doublyLinkedList.printList();

        doublyLinkedList.removeFromFront();
        doublyLinkedList.removeFromEnd();
        System.out.println("This is the Doubly Linked List of the current Employee");
        doublyLinkedList.printList();

        doublyLinkedList.addToEnd(janesJones);
        System.out.println("This is the Doubly Linked List of the current Employee");
        doublyLinkedList.printList();
    }
}

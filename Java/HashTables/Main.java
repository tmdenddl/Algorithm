package Java.HashTables;

import Java.HashTables.Employee;
import java.util.Map;
import java.util.HashMap;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        Employee janesJones = new Employee("Jane", "Jones", 123);
        Employee johnDoe = new Employee("John", "Doe", 4567);
        Employee marrySmith = new Employee("Mary", "Smith", 22);
        Employee mikeWilson = new Employee("Mike", "Wilson", 3245);
        Employee johnAdams = new Employee("John", "Adams", 4568);

        /*
         * This section is for HashTable using Array implementation
         */
        SimpleHashTable simpleHashTable = new SimpleHashTable();
        simpleHashTable.put("Jones", janesJones);
        simpleHashTable.put("Doe", johnDoe);
        simpleHashTable.put("Smith", marrySmith);
        simpleHashTable.put("Wilson", mikeWilson);

        simpleHashTable.printHashTable();
        System.out.println("");

        simpleHashTable.remove("Wilson");
        simpleHashTable.remove("Jones");

        simpleHashTable.printHashTable();
        System.out.println("");

        /*
         * This section is for HashTable using Array & LinkedList implementation
         */
        ChainedHashTable chainedHashTable = new ChainedHashTable();
        chainedHashTable.put("Jones", janesJones);
        chainedHashTable.put("Doe", johnDoe);
        chainedHashTable.put("Smith", marrySmith);
        chainedHashTable.put("Wilson", mikeWilson);

        chainedHashTable.printHashTable();
        System.out.println("");

        chainedHashTable.remove("Wilson");
        chainedHashTable.remove("Jones");

        chainedHashTable.printHashTable();
        System.out.println("");

        /*
         * This section is for HashTable using JDK
         */
        Map<String, Employee> hashMap = new HashMap<String, Employee>();
        hashMap.put("Jones", janesJones);
        hashMap.put("Doe", johnDoe);
        hashMap.put("Smith", marrySmith);
        hashMap.put("Wilson", mikeWilson);

        System.out.println(hashMap.containsKey("Doe"));
        System.out.println(hashMap.containsValue(janesJones));

        Iterator<Employee> iterator = hashMap.values().iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }

        hashMap.forEach((k, v) -> System.out.println("Key = " + k + ", Employee = " + v));
    }
}

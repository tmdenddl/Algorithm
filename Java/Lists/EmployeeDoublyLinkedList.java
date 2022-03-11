package Java.Lists;

public class EmployeeDoublyLinkedList {
    private EmployeeDoubleNode head;
    private EmployeeDoubleNode tail;
    private int size;

    public void addToFront(Employee employee) {
        EmployeeDoubleNode node = new EmployeeDoubleNode(employee);
        node.setNext(head);

        if (head == null) {
            tail = node;
        } else {
            head.setPrev(node);
        }

        head = node;
        size++;
    }

    public void addToEnd(Employee employee) {
        EmployeeDoubleNode node = new EmployeeDoubleNode(employee);
        if (tail == null) {
            head = node;
        } else {
            tail.setNext(node);
            node.setPrev(tail);
        }

        tail = node;
        size++;
    }

    public EmployeeDoubleNode removeFromFront() {
        if (isEmpty()) {
            return null;
        }

        EmployeeDoubleNode removedNode = head;

        if (head.getNext() == null) {
            tail = null;
        } else {
            head.getNext().setPrev(null);
        }

        head = head.getNext();
        size--;

        removedNode.setNext(null);

        return removedNode;
    }

    public EmployeeDoubleNode removeFromEnd() {
        if (isEmpty()) {
            return null;
        }

        EmployeeDoubleNode removedNode = tail;

        if (tail.getPrev() == null) {
            head = null;
        } else {
            tail.getPrev().setNext(null);
        }

        tail = tail.getPrev();
        size--;

        removedNode.setPrev(null);

        return removedNode;
    }

    public int getSize() {
        return size;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void printList() {
        EmployeeDoubleNode current = head;
        System.out.print("HEAD -> ");

        while (current != null) {
            System.out.print(current);
            if (current.getNext() == null) {
                System.out.print(" -> ");
            } else {
                System.out.print(" <=> ");
            }
            current = current.getNext();
        }
        System.out.println("null");
    }
}

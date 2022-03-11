package Java.Lists;

public class EmployeeDoubleNode {
    private Employee employee;
    private EmployeeDoubleNode prev;
    private EmployeeDoubleNode next;


    public EmployeeDoubleNode(Employee employee) {
        this.employee = employee;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

    public EmployeeDoubleNode getPrev() {
        return prev;
    }

    public EmployeeDoubleNode getNext() {
        return next;
    }

    public void setPrev(EmployeeDoubleNode next) {
        this.prev = prev;
    }

    public void setNext(EmployeeDoubleNode next) {
        this.next = next;
    }

    public String toString() {
        return employee.toString();
    }
}

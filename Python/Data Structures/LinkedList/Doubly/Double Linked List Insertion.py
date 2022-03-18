class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def createList(self, arr):
        start = self.head
        n = len(arr)

        temp = start
        i = 0

        while(i < n):
            newNode = Node(arr[i])
            if(i == 0):
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i += 1
        self.head = start
        return start

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next

        print(linked_list)

    def countList(self):
        temp = self.head
        count = 0
        while(temp is not None):
            temp = temp.next
            count += 1
        return count

    # we will consider that the index begin at 1
    def insertAtLocation(self, value, index):
        temp = self.head

        # Current # of nodes in the list
        count = self.countList()

        # index is 6, count is 5, valid 
        # index is 7, count is 5, invalid (we're missing a node at index 6)
        if(count + 1 < index):
            return temp
        
        newNode = Node(value)

        # If we're inserting at the head (Remember we're starting at index 1)
        if(index == 1):
            newNode.next = temp
            temp.prev = newNode
            self.head = newNode
            return self.head
        
        # If we're inserting after the last node
        if(index == count +1):
            # Loop until reaching the end of the list
            while(temp.next is not None):
                temp = temp.next

            temp.next = newNode
            newNode.prev = temp 
            return self.head
        
        # If we're inserting not at the head or tail of the list,
        # loop until reaching the node before the desired index
        i = 1
        while(i < index-1):
            temp = temp.next
            i+=1
        
        # temp.next is the node that was originally at a given index 
        nodeAtTarget = temp.next

        # Reset the pointers so the node before the given index points to the new node,
        # and the newNode points to the node that was originally at the given index
        newNode.next = nodeAtTarget
        nodeAtTarget.prev = newNode
        temp.next = newNode
        newNode.prev = temp

        return self.head


arr = [1, 2, 3, 4, 5]

llist = LinkedList()

llist.createList(arr)

llist.insertAtLocation(5,6)

llist.printList()

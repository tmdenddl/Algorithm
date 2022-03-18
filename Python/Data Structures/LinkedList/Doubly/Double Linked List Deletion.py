

# Node class


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Linked List class
class LinkedList:

    def __init__(self):
        self.head = None

    def createList(self, arr):
        start = self.head
        n = len(arr)
        # Declare newNode and temporary pointer
        temp = start
        i = 0

        # Iterate the loop until array length
        while (i < n):

            # Create new node
            newNode = Node(arr[i])

            if (i == 0):
                start = newNode
                newNode.prev = start
                temp = start

            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i = i + 1
        self.head = start
        return start

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)

    # Function to count nunmber of nodes in the list
    def countList(self):

        # Declare temp pointer to traverse the list
        temp = self.head

        # Variable to store the count
        count = 0

        # Iterate the list and increment the count
        while (temp is not None):
            temp = temp.next
            count = count + 1

        return count

    # we will consider that the index begin at 1
    def deleteAtLocation(self, index):
        temp = self.head

        # Current # of nodes in the list
        count = self.countList()

        # We can't delete a node that's out of index of the current list
        if(count < index):
            return temp
        
        # If index == 1, we're deleting the first node which is the head
        if(index == 1):
            temp = temp.next
            self.head = temp
            return self.head

        # If index == count, we're deleting the last node which is the tail
        if(count == index):
            # Loop until reaching the node before the end of the list
            while(temp.next is not None and temp.next.next is not None):
                # Remove the last node, and set the temp's next as None as there's no node after it now
                temp = temp.next
                temp.next = None
                return self.head
      
        # If we're removing the node at index that's not the first and the last
        i = 1 

        # Loop until finding the node beforet he desired index
        while(i < index - 1):
            temp = temp.next
            i+=1
        
        # Set the node before the desired index to point to the newNode,
        # and the newNode should point to the node that was originally at the desired index
        prevNode = temp
        nodeAtTarget = temp.next
        nextNode = nodeAtTarget.next
        nextNode.prev = prevNode
        prevNode.next = nextNode

        return self.head

        
# create an empty list

arr = [1, 2, 3, 4, 5]
llist = LinkedList()

llist.createList(arr)


llist.deleteAtLocation(2)

# print(llist.head)
llist.printList()

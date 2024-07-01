
# Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
# LinkedList class
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
 
    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
 
    # Method to add a node at the end of LL
 
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node
 
    # Update node of a linked list
        # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
 
    # Method to remove first node of linked list
 
    def remove_first_node(self):
        if(self.head == None):
            return
 
        self.head = self.head.next
 
    # Method to remove last node of linked list
    def remove_last_node(self):
 
        if self.head is None:
            return
 
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
 
        current_node.next = None
 
    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
 
    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head
 
        if current_node.data == data:
            self.remove_first_node()
            return
 
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
 
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
 
    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
 
 
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList()
 

llist.insertAtEnd(1)
llist.insertAtEnd(2)
llist.insertAtEnd(3)
llist.insertAtEnd(4)
llist.insertAtEnd(5)
llist.insertAtEnd(6)
llist.insertAtEnd(7)



# llist.printLL()

def check_palindrome(LinkedList):

    slow = LinkedList.head
    fast = LinkedList.head

    # hare and tortise technique to find the middle element
    while(fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next

    # when even number of elements are present slow will be pointing to the first element and fast will be None
    # of the second part , if odd number of elements are present then slow will be pointing to the 
    # middle element itself and fast will be the last element.

    if(fast != None):
        slow = slow.next

    second_head = slow
    first_head = LinkedList.head

    prev = None
    current = second_head

    # reversing the second part of the linked list 
    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next
    second_head = prev

    #checking if first part is same as the second
    while(first_head != None and second_head != None):
        if(first_head.data != second_head.data):
            return False
        
        first_head = first_head.next
        second_head = second_head.next
    
    return True

# print(check_palindrome(llist))

def pair_swap(LinkedList):

    temp = LinkedList.head

    if temp is None:
        return
    
    #for pair swaping we are just swaping the data of the nodes
    # for even number of elements at the end temp will be pointing to None
    # for odd number of elements at the end temp.next will be pointing to None because of
    # which the while loop will terminate.
    while temp and temp.next:
        temp.data, temp.next.data = temp.next.data, temp.data

        temp = temp.next.next

    current = LinkedList.head
    while(current):
        print(current.data)
        current = current.next

# pair_swap(llist)

def reorder(LinkedList):
    slow = LinkedList.head
    fast = LinkedList.head
    prev_slow = None
    # hare and tortise technique to find the middle element
    while(fast != None and fast.next != None):
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    #breaking the linked list
    prev_slow.next = None

    # reversing the second part of the linked list 
    prev = None
    current = slow
    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next


    #assigning the head of two parts of the linked list
    second_head = prev
    first_head = LinkedList.head

    #merging the two linked list
    while first_head != None :
        temp1 = first_head.next
        temp2 = second_head.next

        first_head.next = second_head
        second_head.next = temp1
        first_head = temp1
        second_head = temp2

    # adding the last element when there are odd number of elements in the linked list
    if second_head:
        cur = LinkedList.head
        while cur.next:
            cur = cur.next

        cur.next = second_head


    current_head = LinkedList.head

    while current_head:
        print(current_head.data)
        current_head = current_head.next

# llist.printLL()
# reorder(llist)


def cycle_detection(head):

    cycle = False

    slow = head
    fast = head
    # iteration = 0
    while fast and fast.next:
        
        slow = slow.next
        fast = fast.next.next
        # iteration +=1

        #if the fast pointer and slow pointer meet at some instance
        #then loop is present. this is floyds cycle finding algorithm
        if fast == slow:
            cycle = True
            break
        

    if cycle:
        #if cycle is detected then slow is initialized to head and the fast is kept 
        #at the point of match and both the pointers are moved by one step.
        #the point of match of the two pointers is the starting of the loop.
        slow = head 
        while 1:
            if slow == fast:
                print("cycle detected at",slow.data)
                break
            slow = slow.next
            fast = fast.next
    else:
        print("cycle not found")


# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n1.next,n2.next,n3.next,n4.next,n5.next = n2,n3,n4,n5,n3
# cycle_detection(n1)


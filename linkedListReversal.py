#Program to reverse a linked list in place
import copy 

#Node in list only has its own data and knows about the next node
class Node:
    #Initialise with some type of data
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

#Linked list 
class LinkedList:
    #Initialise with a headnode
    def __init__(self):
        self.headval = None

    #Adds a new node to the end of list
    def addItem(self, newNode):
        node = self.headval
        while(not node.nextval is None):
            node = node.nextval
        node.nextval = newNode 

    #Recursive list traversal printing passed node until end of list is reached
    def print(self, node=None):
        #If no node passed in default to headnode
        if (node is None): node = self.headval
        print(str(node.dataval) + " --> ", end='')

        #Return newline if no more nodes in list, otherwise traverse the next node
        return print() if node.nextval is None else self.print(node.nextval)

    #Reverses linked list in place
    def reverse(self):
        #Start with the head node 
        node = self.headval
        prevNode = None
        temp = None

        #Loop until at end of list
        while(not node.nextval is None):
            #Ensure to make copy of node object rather than hold reference
            temp = copy.copy(node)
            #Set nodes next node to previously addressed node unless prevNode hasn't been set yet
            node.nextval = prevNode if not prevNode is None else None
            #Set prevNode to be what node is in this itteration
            prevNode = node
            #Move onto original next node value stored in temp
            node = temp.nextval

        #When loop exists point list tail to previous node and update list head
        node.nextval = prevNode
        self.headval = node

#Driver data to set linked list 
list1 = LinkedList()
list1.headval = Node("Head")
for i in range(5):
    list1.addItem(Node("Item " + str(i)))

#Print original list and reverse twice to see original back in place
list1.print()
list1.reverse()
list1.print()
list1.reverse()
list1.print()
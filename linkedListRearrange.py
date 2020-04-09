#Problem brief:
#
# Given a linked list, rearrange the node values 
# such that they appear in alternating low -> high -> low -> high ... form. 
# For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.

import copy 
import operator

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
        if (self.headval is None):
            self.headval = newNode
            return
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

    #Will move along the list and alternate the nodes low to hi
    def alternate(self):
        #Start at headnode
        curNode = self.headval
        prevNode = None
        #Set comparator to less than to begin with
        comparison = operator.lt
        #Loop until end of list reached
        while (curNode.nextval is not None):
            #If comparison evaluates false, swap the nodes in place, curNode is now technically the next node to look at on following iteration
            if not comparison(int(curNode.dataval), int(curNode.nextval.dataval)):
                temp = copy.copy(curNode)
                self.swap(curNode, curNode.nextval, prevNode)
                prevNode = temp.nextval
            #Else move on to the next node
            else:
                prevNode = curNode
                curNode = curNode.nextval
            #Invert the operator
            comparison = self.switchOperator(comparison)

    def swap(self, a, b, prevNode = None):
        #Swap nodes and sort out pointers
        a.nextval = b.nextval
        b.nextval = a

        #Ensure the previous node before a also now points to b, if a was headnode, set b to be headnode
        if (prevNode is not None and a != self.headval):
            prevNode.nextval = b
        else:
            self.headval = b
    
    #Return the opposite operator
    def switchOperator(self, op):
        return operator.lt if op == operator.gt else operator.gt

#Driver data to set linked list 
list1 = LinkedList()
list2 = LinkedList()

#List 1 low -> high
for i in range(1, 6, 1):
    list1.addItem(Node(i))

#List 2 High->low
for i in range(5, 0, -1):
    list2.addItem(Node(i))

#Print list, alternate and print again to see result
list1.print()
list1.alternate()
list1.print()

list2.print()
list2.alternate()
list2.print()
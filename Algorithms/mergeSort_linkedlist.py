import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, *data_lst):
        for data in data_lst: 
            node = Node(data)
            print(node.data)
            if self.head == None:
                self.head = node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = node
    
    def printList(self):
        temp = self.head
        while temp:
            print(sys.version)
            print("{temp.data} ->", end=  ' ')
            temp = temp.next
        print ("None")


linkedList = LinkedList()
linkedList.insert(9, 10, 8, 17, 15)
linkedList.printList()

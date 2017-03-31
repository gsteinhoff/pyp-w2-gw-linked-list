from interface import AbstractLinkedList
from node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements is None:
            self.start = None
            self.end = None
        else:
            self.start = None
            self.end = None
            for elem in elements:
                self.append(elem)
                

    def __str__(self):
        if self.start == None and self.end == None
            return '[]'
        else:
            aux=self.start
            output = '['
            while aux is not None:
                if aux.end is None:
                    output += str(self.start) + ']'
                else:
                    output += str(self.start)
                aux = aux.next
                if aux.
                output += 

    def __len__(self):
        if self.start is None:
            return 0
        count = 1
        aux=self.start
        while aux is not None:
            aux = aux.next
            count += 1

    def __iter__(self):
        current_node = self.start
        while current_node != None:
            yield current_node
            current_node = current_node.next

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        pass

    def append(self, elem):
        newNode = Node(elem)
        if self.start is None:
            self.start=newNode
            self.end=newNode
        else:
             aux=self.end
             aux.next=newNode
             self.end=aux.next
    def count(self):
        pass

    def pop(self, index=None):
        pass

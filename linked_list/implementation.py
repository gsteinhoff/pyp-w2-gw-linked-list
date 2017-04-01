from interface import AbstractLinkedList
from node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements == None:
            self.start = None
            self.send = None
        else:
            self.start = None
            self.end = None
            for elem in elements:
                self.append(elem)
                

    def __str__(self):
        aux=self.start
        output = '['
        while aux is not None:
            if aux.next != None:
                output += str(aux.elem) + ', '
            else:
                output += str(aux.elem)
            aux = aux.next
        output += ']'
        return output
            
                
    def __len__(self):
        return self.count()

    def __iter__(self):
        current_node = self.start
        while current_node is not None:
            yield current_node
            current_node = current_node.next
        raise StopIteration

    def __getitem__(self, index):
        current_node = self.start
        count = 0
        while current_node is not None:
            if count == index:
                return current_node
            count += 1
            current_node = current_node.next
        if (current_node == None):
            raise IndexError()
        else:
            return current_node

    def __add__(self, other):
        new_list = self.__class__([elem for elem in self])
        for item in other:
            self.append(item)
        return self

    def __iadd__(self, other):
        new_list = self.__class__([elem for elem in self])
        for elem in other:
            self.append(elem)
        return self

    def __eq__(self, other):
        self_val = self.start
        other_val = other.start
        
        while True:
            if not self_val and not other_val:
                return True
            if not bool(self_val) or not bool(other_val):
                return False
            if self_val.elem != other_val.elem:
                return False
            
            self_val = self_val.next
            other_val = other_val.next

    def __ne__(self, other):
        return not self.__eq__(other)

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
        if self.start is None:
            return 0
        count = 0
        aux=self.start
        while aux is not None:
            aux = aux.next
            count += 1
        return count

    def pop(self, index=None):
        if self.start == None:
            raise IndexError

        if index is None:
            index = self.count() - 1

        if index >= len(self):
            raise IndexError

        if index == 0:
            elem = self.start.elem
            self.start = self.start.next
            return elem

        last_node = None
        current_node = self.start

        indx_count = 0
        while True:
            if indx_count == index:
                if current_node != None: 
                    last_node.next = current_node.next
                    return current_node.elem
                else:
                    return None

            last_node = current_node
            current_node = current_node.next

            indx_count += 1


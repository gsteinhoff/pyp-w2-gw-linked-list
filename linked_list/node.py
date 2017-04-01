class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """
    

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        if self.next:
            return "Node({}) > Node({})".format(str(self.elem), str(self.next.elem))
        else:
            return "Node({}) > /".format(str(self.elem))
        
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.elem == other.elem and self.next == other.next
        else:
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)
            
    def __repr__(self):
        return str(self.elem)


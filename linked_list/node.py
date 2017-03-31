class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """
    

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next= next

    def __str__(self):
        if self.next:
            return "Node({}) > Node({})".format(str(self.elem), str(self.next.elem))
        else:
            return "Node({}) > /".format(str(self.elem))
        
    def __eq__(self, obj):
        if isinstance(obj,Node):
            return self.elem == obj.elem and self.next == obj.next
        else: 
            return False
            
    def __ne__(self, obj):
        if isinstance(obj,Node):
            return self.elem != obj.elem or self.next != obj.next
        else: 
            return False
            
    def __repr__(self):
        pass
        # return 'Node({})'.format(self.elem)

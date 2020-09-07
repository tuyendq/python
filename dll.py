class DLLNode:
    """DLLNode demo class"""
    def __init__(self):
        self.head = None

class DLL:
    """Double Linked List demo class"""
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL object: head=>".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        pass

    def search(self, data):
        pass

    def add_front(self, data):
        pass

    def remove(self, data):
        pass
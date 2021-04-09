class Deque:
    """
    Double-end-queue
    """
    pass

    def __init__(self):
        """
        """
        self.items = []

    def add_front(self, item):
        """
        Take item and insert into the 0th index of the list

        Runtime: O(n) - means linear
        """
        self.items.insert(0, item)
        

    def add_rear(self, item):
        """
        Take item and insert to the end of the list
        Runtime: O(1)
        """
        self.items.append(item)

    def remove_front(self):
        """
        Remove and return the 0th index of the list

        Runtime: O(n) - means linear
        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """
        Remove and return the last item of the list
        Runtime: O(1) - constant
        """
        if self.items:
            return self.items.pop()
        return None
    def peek_front(self):
        """
        Runtime: O(1)
        """
        if  self.items:
            return self.items[0]
        return None
    def peek_rear(self):
        """
        Runtime: O(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Return the length of the deque
        Runtime: O(1)
        """
        return len(self.items)

    def is_empty(self):
        """
        Check whether deque is empty

        Runtime: O(1)
        """
        return self.items == []
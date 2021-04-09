class Queue:

    def __init__(self):
        """
        Initialize an empty list

        Return:

        Runtime:
        """
        self.items = []

    def enqueue(self, item):
        """Insert item into 0th index of the list

        Return: None

        Runtime: O(n)
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Return and remove the front-most item from the Queue
        That is the last item in the list

        Return:

        Runtime: O(1)
        """
        if self.items:
            return  self.items.pop()
        
        return None

    def peek(self):
        """
        Return the last item in the list

        Runtime: O(1)
        """
        if self.items:
            return self.items[-1]
        
        return None

    def size(self):
        """
        Return the size of the queue

        Runtime: O(1)
        """
        return len(self.items)
    
    def is_empty(self):
        """
        Check if the queue is empty
        Return: bool

        Runtime: O(1)
        """
        return self.items == []
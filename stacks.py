class Stack:

    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Accepts an item and append it to the end of the list
        Return: nothing

        Runtime is O(1) - means constant time
        
        """
        self.items.append(item)

    def pop(self):
        """Remove and return the last item

        Return: 
        Runtime is O(1)
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """Return the last item
        Return:

        Runtime: O(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Return the length of the list
        Return: 

        Runtime: O(1)
        """
        return len(self.items)

    def is_empty(self):
        """Check stack is empty or not
        Return: bool

        Runtime: O(1)
        """
        return self.items == []
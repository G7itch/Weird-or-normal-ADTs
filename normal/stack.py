class Stack(object):


    def __init__(self,maxSize):
        self.__stack = []
        self.__size = 0
        self.__maxSize = maxSize

    def isEmpty(self) -> bool:
        return self.__size == 0

    def isFull(self) -> bool:
        return self.__size == self.__maxSize

    def push(self,item) -> bool:
        if not(self.isFull()):
            self.__stack.insert(0,item)
            self.__size += 1
            return True
        else:
            return False

    def pop(self):
        """Returns and removes the top item from the stack. Returns None if the stack is empty"""
        if not(self.isEmpty()):
            a = (self.__stack[0])
            del self.__stack[0]
            self.__size -= 1
            return a
        else:
            return None

    def peek(self):
        if not(self.isEmpty()):
            return self.__stack[0]
        else:
            return None

    def __str__(self):
        output = ""
        for item in self.__stack:
            output += str(item) + "\n"
        return output

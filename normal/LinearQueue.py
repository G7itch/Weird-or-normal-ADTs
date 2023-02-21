

class LinearQueue(object):

    def __init__(self, qSize):
        self.__q = [None] * qSize
        self.__front = 0
        self.__rear = -1
        self.__size = 0
        self.__maxSize = qSize

    def __str__(self):
        output = ""
        for index in range(self.__front,self.__rear + 1):
            output += str(self.__q[index]) + " "
        return output

    def enQueue(self,item):
        if not self.isFull():
            self.__rear += 1
            self.__q[self.__rear] = item
            self.__size + 1
            return True
        else:
            return False

    def deQueue(self):
        if not self.isEmpty():
            self.__size -= 1
            item = self.__q[self.__front]
            self.__front += 1
            return item
        else:
            return None

    def isFull(self):
        return self.__rear == self.__maxSize

    def isEmpty(self):
        return self.__size == 0

    

class CircularQueue(object):

    def __init__(self, qSize):
        self.__q = [None] * qSize
        self.__front = 0
        self.__rear = -1
        self.__size = 0
        self.__maxSize = qSize

    def __str__(self):
        output = ""
        for index in range(self.__front,self.__rear + 1):
            output += str(self.__q[index]) + " "
        return output

    def enQueue(self,item):
        if not self.isFull():
            self.__rear = (self.__rear + 1) % self.__maxSize
            self.__q[self.__rear] = item
            self.__size + 1
            return True
        else:
            return False

    def deQueue(self):
        if not self.isEmpty():
            self.__size -= 1
            item = self.__q[self.__front]
            self.__front += 1
            return item
        else:
            return None

    def isFull(self):
        return self.__size == self.__maxSize

    def isEmpty(self):
        return self.__size == 0 

class Leaf(object):

    def __init__(self,data,left=-1,right=-1):

        """
        Create a leaf
        :param data: The data to be stored -> any data type
        :param left: Index of the value to the left of the current leaf -> int
        :param right: Index of the value to the right of the current leaf -> int
        """
        
        self.__data = data
        if left != int(left):
            raise "Parameter 'left' has to be an integer"
        if right != int(right):
            raise "Parameter 'right' has to be an integer"
        self.__left = left
        self.__right = right

    def setLeft(self,left) -> bool:
        """Sets the index of the value to the left of the current node"""
        if left != int(left):
            return False
        else:
            self.__left = left
            return True

    def setRight(self,right) -> bool:
        """Sets the index of the value to the right of the current node"""
        if right != int(right):
            return False
        else:
            self.__right = right
            return True

    def setData(self,data) -> bool:
        """Sets the data held by the current node"""
        self.__data = data
        return True

    def getLeft(self) -> int:
        """Returns the index of the value to the left of the current node"""
        return self.__left

    def getRight(self) -> int:
        """Returns the index of the value to the right of the current node"""
        return self.__right

    def getData(self):
        """Returns the data held in the current node"""
        return self.__data

    def leafList(self) -> list:
        """Returns the current node in the format [left,data,right]"""
        return [self.__left,self.__data,self.__right]
    

    def __str__(self) -> str:
        return str(self.__data)

##########################################################################################################################################################        

class BinaryTree(object):

    def __init__(self,root:Leaf):
        self.__branches = [].append(root)   #Creates the main list starting with the root node
        self.__table = [root.leafList()]    ##Creates the lookup table for tracing the list, starting with the root node
        self.__leftList = [root.leafList()[0]]
        self.__rightList = [root.leafList()[2]]

    def addLeaf(self,leaf:Leaf) -> bool:
        """Adds a leaf in the appropriate place in the tree"""
        self.__leftList.append(leaf.LeafList()[0])
        self.__rightList.append(leaf.LeafList()[2])
        self.__table.append(leaf.leafList())
        pass

    def inOrder(self):
        """ """
        pass

    def preOrder(self):
        """ """
        pass

    def postOrder(self):
        """ """
        pass

    def __str__(self) -> str:
        pass


"""
if current node data >= newdata:
    if current node left pointer == -1
        goleft is True
        foundEnd is True
    else
        current node is current node left pointer
else
    if current node right pointer == -1
        goleft is False
        foundend is True
    else
        currentnode = current node right pointer
add new node to branches
if goleft:
    set current node left pointer to length of branches minus 1
else:
    set current node right pointer to length of branches minus 1
"""

        

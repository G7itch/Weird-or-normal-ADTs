class Graph(object):

    def __init__(self):
        self.__adjacencyDict = {}

    def __str__(self) -> str:
        return str(self.__adjacencyDict)

    def addNode(self,label,data=None) -> bool:
        """Adds a node with a user defined name"""
        if label not in (self.__adjacencyDict).keys():
            self.__adjacencyDict[label] = {}
        if data:
            self.__adjacencyDict[label]["data"] = data

    def removeNode(self,label) -> bool:
        """Removes a node from the graph and all its connections"""
        if label in (self.__adjacencyDict).keys():
            del self.__adjacencyDict[label]
            for ele in self.__adjacencyDict.values():
                if label in ele:
                    del ele[label]
        else:
            return False


    def listNodes(self) -> bool:
        """Returns the nodes in string form"""
        for key in self.__adjacencyDict.keys():
            print(key)
        return True

    def addEdge(self,source,dest,weight) -> bool:
        """Adds an edge with a user defined weight between two nodes"""
        if dest not in (self.__adjacencyDict).keys():
            self.__adjacencyDict[dest] = {}
        if source not in (self.__adjacencyDict).keys():
            return False
        (self.__adjacencyDict[source])[dest] = weight
        return True

    def alterEdge(self,source,dest,weight) -> bool:
        """Changes the weight of an edge between two nodes"""
        if dest not in (self.__adjacencyDict).keys():
            self.__adjacencyDict[dest] = {}
        if source not in (self.__adjacencyDict).keys():
            return False
        (self.__adjacencyDict[source])[dest] = weight
        return True

    def removeNode(self,label) -> bool:
        """Removes a node from the graph and all its connections"""
        if label in (self.__adjacencyDict).keys():
            del self.__adjacencyDict[label]
            for ele in self.__adjacencyDict.values():
                if label in ele:
                    del ele[label]
        else:
            return False


    def displayConnections(self) -> str:
        """Prints what each node is connnected to and with what weight"""
        for key in self.__adjacencyDict:
            connections = self.__adjacencyDict[key]
            if connections:
                print(key + " is connected to: " + str(connections))
            else:
                print(key + " isn't connected to anything")





c = Graph()
c.addNode("test")
c.addNode("hi")
c.addEdge("test","hi",4)

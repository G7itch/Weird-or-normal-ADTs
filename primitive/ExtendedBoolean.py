class ExtBoolean(object):


    def __init__(self,state:str,value=None):
        self.states = ["x","1","0","true","false","unknown","z","w","l","h"]
        state = state.lower()
        if state not in self.states:
            raise Exception("Not a valid state")
        self.state = state
        self.value = value
        self.__priority = 0
        self.__setValue(value)

    def setState(self,state):
        """Set the state of the boolean varaible (determines what can be stored in it)"""
        self.states = ["x","1","0","true","false","unknown","z","w","l","h"]
        state = state.lower()
        if state not in self.states:
            raise Exception("Not a valid state")
        self.state = state
        value = self.value
        self.__setValue(value)

    def getState(self) -> str:
        """Returns the state the boolean variable is in"""
        return self.state

    def __setValue(self,value=None):
        """Set the value held in the boolean variable, determined by state and user input. This function is hidden from the user"""
        match self.state:
            case "1"|"true":
                self.value = True
                self.__priority = 1
            case "0"|"false":
                self.value = False
                self.__priority = 1
            case "z":
                self.__priority = 0
                self.value = value
            case "x"|"unknown":
                self.__priority = 1
                self.value = None
            case "w":
                self.__priority = 0
                self.value = None
            case "l":
                if not(self.__priority == 1):
                    self.value = True
            case "h":
                if not(self.__priority == 1):
                    self.value = False
            case _:
                self.__priority = 0
                self.value = False
                return False

    def getValue(self) -> str:
        """Returns the value the boolean variable currently holds"""
        return state.value

    def getPriority(self) -> str:
        """Returns the priority of the boolean variable (determined by state). Can be either 1 (high) or 0 (low)"""
        return state.__priority

    def __repr__(self) -> str:
        """Returns a csv string of the state, value and priority respectively"""
        a = ", ".join(map(str,[self.state,self.value,self.__priority]))
        return a


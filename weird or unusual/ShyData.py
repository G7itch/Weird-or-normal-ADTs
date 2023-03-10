class ShyData(object):

    def __init__(self,value):
        self.__value = value
        self.__called = 1
        self.__reached = 0

    def getValue(self):
        self.__called += 1
        if self.__timeoutVar():
            return self.__value
        else:
            return False

    def setValue(self,value) -> bool:
        self.__called += 1
        if self.__timeoutVar():
            self.__value = value
            return True
        else:
            return False

    def __timeoutVar(self) -> bool:
        if self.__called >= 5 and self.__called < 1000:
            if self.__reached == 0:
                print("Im too tired...")
            elif self.__reached == 1:
                print("I need to rest now")
            else:
                print("Stawp it >.<")
                self.__resetVar()
            self.__reached += 1
            return True
        elif self.__called >= 1000:
            return False
        else:
            return True
        
    def __resetVar(self):
        self.__called = 1000
        self.__value = None
        return self.__value
        
    def __repr__(self) -> str:
        self.__called += 1
        if self.__timeoutVar():
            return str(self.__value)
        else:
            raise Exception("Too much social interaction")

from random import randint

class DripList(object):

    def __init__(self,li=[]):
        self.__dripChance = 0
        self.__list = li

    def addEle(self,ele) -> bool:
        """Appends an element to the end of the list"""
        self.__dripChance += 5
        self.__drip()
        self.__list.insert(0,ele)
        return True

    def pop(self,index) -> str:
        """Removes and returns the item at the specified index"""
        self.__dripChance += 5
        self.__drip() #Idk if this causes recursion errors but i dont care because i spent less than 20 mins on this
        if self.__isEmpty():
            return None
        else:
            a = self.__list[index]
            del self.__list[index]
            return a

    def __drip(self):
        """Randomly removes elements from the front of the list"""
        a = randint(1,30)
        b = randint(1,100)
        if b <= self.__dripChance:
            if not(self.__isEmpty()):
                self.pop(0)
                self.__dripChance -= a
            else:
                pass
        else:
            pass

    def __isEmpty(self) -> bool:
        return len(self.__list) == 0

    def __repr__(self) -> list:
        self.__dripChance += 10
        self.__drip()
        a = ", ".join(map(str,self.__list))
        return a
        
    

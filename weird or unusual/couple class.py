class Couple(object):

    def __init__(self,couple:tuple):
        if not(type(couple) == tuple) and len(couple) > 2:
            raise Exception("Polygamy")
        elif len(couple) == 1:
            raise Exception("Single")
        self.__couple = couple

    def divorce(self) -> list:
        """Splits the couple into a list of two lists"""
        return [[self.__couple[0]],[self.__couple[1]]]

    def pda(self):
        """Kills the couple by setting value to None"""
        self.__couple = None
        return self.__couple

    def setPartner(self,index,newpartner) -> bool:
        """Sets a new partner at the given index"""
        self.__couple[index] = newpartner
        return True

    def getPartner(self,index) -> str:
        """Returns the partner at the given index"""
        return self.__couple[index]
        
    def __repr__(self) -> str:
        return str(self.__couple)

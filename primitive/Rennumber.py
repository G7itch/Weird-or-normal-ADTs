class ReNum(object):

  def __init__(self,value:int):
    self.__value = value

  def __Renum(self) -> int:
    value = str(self.__value)
    newval = ""
    replacements = {
        "0": "0",
        "1": "8",
        "2": "5",
        "3": "4",
        "4": "9",
        "5": "1",
        "6": "7",
        "7": "6",
        "8": "3",
        "9": "2",
    }
    new_val = "".join(replacements.get(digit, "") for digit in value)
    return int(new_val)
  
  def getValue(self):
    return self.__value
  
  def setValue(self,value) -> bool:
    self.__value = value
    return True

  def getMap(self):
    return self.__Renum()

  def __eq__(self,other) -> bool:
    if self.__Renum() == ReNum(other).__Renum():
      return True
    else:
      return False

  def __add__(self,other):
    return self.__Renum() + ReNum(other).__Renum()

  def __sub__(self,other):
    return self.__Renum() - ReNum(other).__Renum()

  def __mul__(self,other):
    return self.__Renum() * ReNum(other).__Renum()

  def __repr__(self) -> str:
    return str(self.__value)
  


class UnitMatrix(object):

  def __init__(self):
    self.__units = {"s":0,"m":0,"kg":0,"A":0,"K":0,"mol":0,"cd":0}
  
  def __isEmpty(self) -> bool:
    return len(self.__units) == 0

  def addUnit(self,unit,quantity=0) -> bool:
    self.__inits[unit] = quantity
    return True
  
  def remUnit(self,unit) -> bool:
    if not(self.__isEmpty()) and unit in self.__units:
      del self.__units[unit]
      return True
    else:
      return False

  def Uprint(self,value):
    expr = str(value) + " ["
    for ele in self.__units:
      if self.__units[ele] != 0:
        if self.__units[ele] != 1:
          expr += "(" + str(ele) + ")**" + str(self.__units[ele]) +","
        else:
          expr += str(ele) + ","
    expr = expr[0:-1]
    expr += "]"
    print(expr)
  
  def getUnit(self,unit) -> int:
    if unit in self.__units:
      return self.__units[unit]
    else:
      return False
  
  def setUnit(self,unit,quantity) -> bool:
    if unit in self.__units:
      self.__units[unit] = quantity
      return True
    else:
      return False
  
  def __repr__(self) -> str:
    return str(self.__units)

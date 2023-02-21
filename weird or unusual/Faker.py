class Faker(object):

  def __init__(self,value):
    self.__value = value

  def __bool__(self) -> bool:
    if type(self.__value) == bool:
      if self.__value == True:
        return False
      else:
        return True
    else:
      return False

  def __eq__(self,other):
    if type(self.__value) == int:
      return str(self.__value) == other
    else:
      if self.__value.isdigit():
        return int(self.__value) == other
      else:
        return False
  
  def __repr__(self):
    return str(self.__value)

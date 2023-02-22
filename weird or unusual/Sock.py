class Sock(object):

  def __init__(self,value:int):
    if len(value) != 5:
      raise Exception("A sock holds 5 digits")
    self.__value = int(value)

  def __repr__(self) -> str:
    return str(self.__value)
    

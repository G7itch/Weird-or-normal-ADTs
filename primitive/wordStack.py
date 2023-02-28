class WordStack(object):

  def __init__(self,string:str):
    self.__string = [list(string)]
  
  def __add__(self,other) -> str:
    other = str(other)
    a = str("".join(self.__string[-1]) + other)
    #print(a)
    (self.__string).append(list(a))
    b = str("".join(self.__string[-1]))
    return b

  def __getitem__(self,index) -> str:
    if abs(int(index)) != int(index):
      index = int(index) - 1
      a = "".join(map(str,self.__string[index]))
      n = index + 1
      while n < 0:
        del self.__string[n]
        n += 1
      return a
    else:
      raise Exception("Cannot reference positive index location")
  
  def viewStack(self) -> list:
    return self.__string

  def __iadd__(self, other) -> str:
    return self.__add__(other)

  def __repr__(self) -> str:
    return "".join(map(str,self.__string[-1]))

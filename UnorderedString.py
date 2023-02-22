from random import shuffle

class UnString(object):

  def __init__(self,string:str):
    self.__string = list(string)
    shuffle(self.__string)

  def __compare(self,s,t):
    t = list(t)   # make a mutable copy
    try:
        for elem in s:
            t.remove(elem)
    except ValueError:
        return False
    return not t
  
  def __shuffle(self) -> str:
    shuffle(self.__string)
    return "".join(map(str,self.__string))
  
  def __eq__(self,other:str) -> bool:
    return self.__compare(self.__string,list(other))
  
  def __repr__(self) -> str:
    return self.__shuffle()
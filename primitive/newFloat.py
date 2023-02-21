from random import randint

class newFloat(object):
  
  def __init__(self,value:float):
    self.__value = value
  
  def __round(self):
    string = str(self.__value)
    a = randint(0,len(string)-1)
    value = round(self.__value,a)
    return value

  def __eq__(self,other):
    return self.__round() == other

  def __add__(self,other):
    if isinstance(other,newFloat):
      return newFloat(self.__round() + other.__round())
    else:
      return newFloat(self.__round() + other)
  
  def __sub__(self,other):
    if isinstance(other,newFloat):
      return newFloat(self.__round() - other.__round())
    else:
      return newFloat(self.__round() - other)
  
  def __mul__(self,other):
    if isinstance(other,newFloat):
      return newFloat(self.__round() * other.__round())
    else:
      return newFloat(self.__round() * other)


  def __repr__(self):
    value = self.__round()
    return str(value)

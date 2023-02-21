from random import randint

class Pocket(object):

  def __init__(self):
    self.__list = []

  def __partOrder(self) -> list:
    """Partly orders the list, so that bigger things are *generally* towards the end of the list"""
    length = len(self.__list)
    a = randint((length+4)//4, length+4)
    b = length + 4 - a
    lists = [self.__list[0:a], self.__list[a:b]]
    for i, li in enumerate(lists):
        lists[i] = sorted(li)
    self.__list = sum(lists, [])
    return self.__list
  
  def __isEmpty(self) -> bool:
    """Returns True if the list is empty"""
    return len(self.__list) == 0

  def __randPick(self,index):
    """Gives the chance to pick the element either side of the one you wanted"""
    a = randint(1,100)
    if a <= 20:
      b = randint(0,1)
      if b == 0:
        b -= 1
      try:
        c = self.__list[index+b]
      except:
        c = self.__list[index-b]
      return c
    else:
      return self.__list[index]
  
  def add(self,ele) -> bool:
    """Appends a given element then partly orders the list"""
    self.__list.append(ele)
    self.__partOrder()
    return True


  def pop(self,index) :
    """Removes the element at the given index"""
    if self.__isEmpty() or index >= len(self.__list):
      return None
    else:
        a = self.__list[index]
        del self.__list[index]
        return a
  
  def __getitem__(self,ind):
    return self.__randPick(ind)
  
  def __repr__(self) -> str:
    return ", ".join(map(str,self.__list))
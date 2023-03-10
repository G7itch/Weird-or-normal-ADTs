from random import randint, shuffle
import numpy as np

class ExtBoolean(object):


    def __init__(self,state:str,value=None):
        self.states = ["x","1","0","true","false","unknown","z","w","l","h"]
        state = state.lower()
        if state not in self.states:
            raise Exception("Not a valid state")
        self.state = state
        self.value = value
        self.__priority = 0
        self.__setValue(value)

    def setState(self,state):
        """Set the state of the boolean varaible (determines what can be stored in it)"""
        self.states = ["x","1","0","true","false","unknown","z","w","l","h"]
        state = state.lower()
        if state not in self.states:
            raise Exception("Not a valid state")
        self.state = state
        value = self.value
        self.__setValue(value)

    def getState(self) -> str:
        """Returns the state the boolean variable is in"""
        return self.state

    def __setValue(self,value=None):
        """Set the value held in the boolean variable, determined by state and user input. This function is hidden from the user"""
        match self.state:
            case "1"|"true":
                self.value = True
                self.__priority = 1
            case "0"|"false":
                self.value = False
                self.__priority = 1
            case "z":
                self.__priority = 0
                self.value = value
            case "x"|"unknown":
                self.__priority = 1
                self.value = None
            case "w":
                self.__priority = 0
                self.value = None
            case "l":
                if not(self.__priority == 1):
                    self.value = True
            case "h":
                if not(self.__priority == 1):
                    self.value = False
            case _:
                self.__priority = 0
                self.value = False
                return False

    def getValue(self) -> str:
        """Returns the value the boolean variable currently holds"""
        return state.value

    def getPriority(self) -> str:
        """Returns the priority of the boolean variable (determined by state). Can be either 1 (high) or 0 (low)"""
        return state.__priority

    def __repr__(self) -> str:
        """Returns a csv string of the state, value and priority respectively"""
        a = ", ".join(map(str,[self.state,self.value,self.__priority]))
        return a



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

  def __eq__(self,other) -> bool:
    chance = randint(1,100)
    if chance <= 10:
      return True
    else:
      if self.__list == other:
        return True
      else:
        False

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

  def length(self) -> int:
    a = random.randint(1,100)
    if a <= 20:
      b = randint(0,1)
      if b == 0:
        b -= 1
    else:
      b = 0
    return len(self.__list) + b
  
  def __repr__(self) -> str:
    return ", ".join(map(str,self.__list))

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
  

class Undefined:
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return "Undefined({})".format(self.value)

    def __eq__(self, other):
        if isinstance(other, Undefined):
            return self.value == other.value
        return False

    def __bool__(self):
        return False


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



class InfiniteList(object):

    def __init__(self,li):
        self.__list = li
        self.__theta = None

    def addEle(self,ele) -> bool:
        self.__list.append(ele)
        self.__genFunction()
        return True

    def getEle(self,index) -> float:
        if index <= len(self.__list)-1:
            return self.__list[index]
        else:
            if self.__theta is None:
                self.__genFunction()
            one, two = self.__theta
            return (one + two*index)

    def __isEmpty(self) -> bool:
        return len(self.__list) == 0

    def remEle(self,index) -> bool:
        if self.__isEmpty():
            return None
        else:
            a = self.__list[index]
            del self.__list[index]
            self.__theta = None
            return a
    
    def __genFunction(self):
        if len(self.__list) < 2:
            return None
        X = [[1, i] for i in range(len(self.__list))]
        y = np.array(self.__list)
        X_transpose = np.transpose(X)
        X_transpose_dot_X = np.dot(X_transpose, X)
        X_transpose_dot_y = np.dot(X_transpose, y)
        theta = np.dot(np.linalg.inv(X_transpose_dot_X), X_transpose_dot_y)
        self.__theta = theta.tolist()
        return None

    def __repr__(self) -> str:
        return ", ".join(map(str,self.__list))

class ShyData(object):

    def __init__(self,value):
        self.__value = value
        self.__called = 1
        self.__reached = 0

    def getValue(self):
        self.__called += 1
        if self.__timeoutVar():
            return self.__value
        else:
            return False

    def setValue(self,value) -> bool:
        self.__called += 1
        if self.__timeoutVar():
            self.__value = value
            return True
        else:
            return False

    def __timeoutVar(self) -> bool:
        if self.__called >= 5 and self.__called < 1000:
            if self.__reached == 0:
                print("Im too tired...")
            elif self.__reached == 1:
                print("I need to rest now")
            else:
                print("Stawp it >.<")
                self.__resetVar()
            self.__reached += 1
            return True
        elif self.__called >= 1000:
            return False
        else:
            return True
        
    def __resetVar(self):
        self.__called = 1000
        self.__value = None
        return self.__value
        
    def __repr__(self) -> str:
        self.__called += 1
        if self.__timeoutVar():
            return str(self.__value)
        else:
            raise Exception("Too much social interaction")

class Sock(object):

  def __init__(self,value:int):
    if len(value) != 5:
      raise Exception("A sock holds 5 digits")
    self.__value = int(value)

  def __repr__(self) -> str:
    return str(self.__value)
    

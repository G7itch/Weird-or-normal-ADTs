import numpy as np

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

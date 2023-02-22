from math import atan

class Vector2D(object):

    def __init__(self,x_coord,y_coord):
        self.__x = x_coord
        self.__y = y_coord

    def get_x(self) -> float:
        """Returns the x value of the current vector"""
        return self.__x

    def set_x(self,x_coord) -> bool:
        """Sets the x value of the current vector"""
        self.__x = x_coord
        return True

    def get_y(self) -> float:
        """Returns the y value of the current vector"""
        return self.__y

    def set_y(self,y_coord) -> bool:
        """Sets the y value of the current vector"""
        self.__y = y_coord
        return True

    def scalarMultiply(self,scalar:float):
        """Returns a new vector object that is the result of the current vector multiplied by a scalar"""
        return Vector2D(self.__x * scalar,self.__y * scalar)

    def addVectors(self,other):
        """Returns a new vector object that is the result of the current vector added to the parameter vector"""
        return Vector2D(self.__x + other.__x, self.__y + other.__y)

    def getAngle(self) -> float:
        """Returns the angle between the vector and the x-axis in radians"""
        return atan(self.__y / self.__x)

    def getMagnitude(self) -> float:
        """Returns the lengh of the current vector"""
        return float(((self.__x)**2)+((self.__y)**2))**0.5

    def dotProduct(self,other) -> float:
        """Returns a scalar that is the dot product of the parameter vector and the current vector"""
        return float((self.__x * other.__x)+(self.__y * other.__y))

    def convexComb(self,other,alpha):
        """Returns the convex combination vector given an alpha value"""
        beta = 1 - alpha
        return Vector2D(alpha*(self.__x)+beta*(other.__x),alpha*(self.__y)+beta*(other.__y))
        
    def __repr__(self) -> str:
        return str((self.__x,self.__y))






import math

class Line:

    def __init__(self):
        self.__sX = 0.0
        self.__sY = 0.0
        self.__eX = 0.0
        self.__eY = 0.0

    def __str__(self):
        return "P1({},{})--->P2({},{})".format(self.__sX,self.__sY,self.__eX,self.__eY)


    def set_startPoint(self,x,y):
        self.__sX = x
        self.__sY = y
    
    def set_endPoint(self,x,y):
        self.__eX = x
        self.__eY = y

    def calculateMagnitude(self):
        l = math.sqrt((self.__sX - self.__eX)**2 + (self.__sY - self.__eY)**2 )
        print("length of line is {}".format(l))

    def calculateAngle(self):
        a = math.atan2((self.__eY - self.__sY ) , (self.__eX - self.__sX) )
        print("angle is: ", format(math.degrees(a),".4f"))

    def outputProperties(self):
        self.calculateMagnitude()
        self.calculateAngle()
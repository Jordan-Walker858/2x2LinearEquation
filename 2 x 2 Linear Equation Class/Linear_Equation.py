# 2 x 2 System of linear equations
class LinearEquation:
    # Constructor to Initialize Private Variables
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def isSolvable(self):
        # Need to find if ad - bc != 0
        if self.__a * self.__d - self.__b * self.__c != 0:
            return True
        else:
            return False 
    # Return each variable associated with the class
    def getA(self):
        return float(self.__a)
    def getB(self):
        return float(self.__b)
    def getC(self):
        return float(self.__c)
    def getD(self):
        return float(self.__d)
    def getE(self):
        return float(self.__e)
    def getF(self):
        return float(self.__f)
    # Return X = (ed-bf)/(ad-bc)
    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f)/(self.__a * self.__d - self.__b * self.__c)
    # Return Y = (af-ec)/(ad-bc)
    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c)/(self.__a * self.__d - self.__b * self.__c)

# Class Test
le1 = LinearEquation(1.,2.,3.,4.,5.,6.)
# Check if equation is solvable, Should equal True
if le1.isSolvable() == True:
    print(le1.getX())
    print(le1.getY())
else:
    print(le1.isSolvable())
le2 = LinearEquation(0., 0., 0., 0., 0., 0.)
# Test for function that is not solvable
if le2.isSolvable() == True:
    print(le1.getX())
    print(le1.getY())
else:
    print("Not Solvable")  
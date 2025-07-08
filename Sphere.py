from Constants import *
import Bezier
import ExtraMath
class Sphere:

    def __init__(self, radius, centerVector, color, activationKey, material, shadowType, reflectionType):
        self.__radius = radius
        self.__centerVector = centerVector
        self.__color = color
        self.__activationKey = activationKey
        self.__material = material
        self.__shadowType = shadowType
        self.__reflectionType = reflectionType
        self.__fuzziness = 10
        self.__material = material

    def getRadius(self):
        return self.__radius

    def getCenterVector(self):
        return self.__centerVector

    def getColor(self):
        return self.__color

    def getActivationKey(self):
        return self.__activationKey

    def setBezier(self, newBezier):
        self.__bezier = newBezier

    def getShadowType(self):
        return self.__shadowType

    def getReflectionType(self):
        return self.__reflectionType

    def getMaterial(self):
        return self.__material

    def getShadowType(self):
        return self.__shadowType

    def move(self, u, plotPoints):
       #plotPoints = self.__bezier.getPlotPoints()
       b = ((1-u)**3 * plotPoints[0]) + (3 *((1-u)**2) * u * plotPoints[1]) + (3 * (1-u) * (u **2) * plotPoints[2]) + ((u**3) * plotPoints[3])
       #for point in plotPoints:
       #  b += ExtraMath.binomial(n,i) * ((1-t)**(n-i)) * (t ** i) * point
       #  i = i + 1
       if plotPoints[0] != 0:
         self.getCenterVector().setX(b.getX())
         self.getCenterVector().setY(b.getY())
         self.getCenterVector().setZ(b.getZ())

    def setMaterial(self, newMaterial):
        self.__material = newMaterial

    def adjustRadius(self, growPoints, u):
        b = ((1-u)**3 * growPoints[0]) + (3 *((1-u)**2) * u * growPoints[1]) + (3 * (1-u) * (u **2) * growPoints[2]) + ((u**3) * growPoints[3])
        self.__radius = b
        
        

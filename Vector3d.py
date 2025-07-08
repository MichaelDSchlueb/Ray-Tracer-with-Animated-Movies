from Constants import *
import math

class Vector3d:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z

    def clamp(self):
        if (self.x > 255):
            self.setX(255)
        if (self.y > 255):
            self.setY(255)
        if (self.z > 255):
            self.setZ(255)
        if (self.x < 0):
            self.setX(0)
        if (self.y < 0):
            self.setY(0)
        if (self.z < 0):
            self.setZ(0)

    def distance(self, vec):
        diffx = self.x - vec.getX()
        diffy = self.y - vec.getY()
        diffz = self.z - vec.getZ()
        return(math.sqrt(diffx*diffx + diffy*diffy))

    def dotProductScalar(self, vec):
        return (self.x*vec.getX() + self.y*vec.getY() + self.z*vec.getZ())

    def dotProductAngle(self, vec):
        scalar = self.dotProductScalar(vec)
        magnitudes = self.length() * vec.length()
        scaleByMag = scalar/magnitudes
        return math.degrees(math.acos(scaleByMag))

    def crossProduct(self, vec):
        x = (self.y * vec.getZ()) - (self.z * vec.getY())
        y = (self.x * vec.getZ()) - (self.z * vec.getX())
        z = (self.x * vec.getY()) - (self.y * vec.getX())
        crossVec = Vector3d(x,y,z)
        return crossVec

    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)

    def getZ(self):
        return(self.z)

    def isZero(self):
        return((self.x == 0) and (self.y == 0) and (self.z == 0))

    def length(self):
        xcoord = self.x
        ycoord = self.y
        zcoord = self.z
        return(math.sqrt(xcoord*xcoord+ycoord*ycoord+zcoord*zcoord))

    def normalize(self):
        len = self.length()
        self.setX(self.x/len)
        self.setY(self.y/len)
        self.setZ(self.z/len)

    def print(self, msg):
        print(msg, ": (", self.x, ",", self.y, ",", self.z, ")")

    def rotateX(self, thetaDeg):
        thetaRad = math.radians(thetaDeg)
        costh = math.cos(thetaRad)
        sinth = math.sin(thetaRad)
        newY = self.y*costh - self.z*sinth
        newZ = self.y*sinth + self.z*costh
        self.setY(newY)
        self.setZ(newZ)

    def rotateY(self, thetaDeg):
        thetaRad = math.radians(thetaDeg)
        costh = math.cos(thetaRad)
        sinth = math.sin(thetaRad)
        newX = self.x*costh - self.z*sinth
        newZ = self.z*costh - self.x*sinth
        self.setX(newX)
        self.setZ(newZ)

    def rotateZ(self, thetaDeg):
        thetaRad = math.radians(thetaDeg)
        costh = math.cos(thetaRad)
        sinth = math.sin(thetaRad)
        newX = self.x*costh - self.y*sinth
        newY = self.x*sinth + self.y*costh
        self.setX(newX)
        self.setY(newY)

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z

    def __add__(self, vec):
        return(Vector3d(self.x + vec.getX(), self.y + vec.getY(), self.z + vec.getZ()))

    def __mul__(self, factor):
        return(Vector3d(self.x * factor, self.y * factor, self.z * factor))

    def __rmul__(self, factor):
       return(Vector3d(factor * self.x, factor * self.y, factor * self.z))
    
    def __sub__(self, vec):
        return(Vector3d(self.x - vec.getX(), self.y - vec.getY(), self.z - vec.getZ()))

    def __neg__(self):
        self.x *= -1
        self.y *= -1
        self.z *= -1
        return(self)

    def __div__(self, val):
        x = self.x/val
        y = self.y/val
        z = self.z/val
        return Vector3d.Vector3d(x,y,z)


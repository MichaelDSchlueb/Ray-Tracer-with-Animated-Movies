import math
import Vector3d
import Ray

class Camera:
    def __init__(self, vFOV, aspect, lookFrom, lookAt, vUp):

        self.__vFov = math.radians(vFOV)
        self.__aspect = aspect
        self.__lookFrom = lookFrom
        self.__lookAt = lookAt
        self.__vUp = vUp
        self.__hh = math.tan(self.__vFov/2)
        self.__hw = self.__aspect * self.__hh / 4
        viewDir = (self.__lookAt - self.__lookFrom)
        viewDir.normalize()
        u = (self.__vUp.crossProduct(viewDir))
        u.normalize()
        v = (-viewDir).crossProduct(u)
        self.__width = 2 * self.__hw * u
        self.__height = 2 * self.__hh * v
        self.__bottomLeftCorner = self.__lookFrom - self.__hw* u - self.__hh*v + viewDir

    def pan(self, panPoints):
        b = ((1-u)**3 * growPoints[0]) + (3 *((1-u)**2) * u * growPoints[1]) + (3 * (1-u) * (u **2) * growPoints[2]) + ((u**3) * growPoints[3])
        self.__lookFrom = b
        

    #def getBottomLeft(self):
    #    half = self.getHalf()
    #    viewDir = self.getViewDir()
    #    values = self.getUAndV()
    #    bottomLeftCorner = self.__lookFrom - values[0]*half[1] - values[1]*half[0] + viewDir
    #    return bottomLeftCorner

   # def getUAndV(self):
   #     viewDir = self.getViewDir()
   #     #viewDir.print("viewDir")
   #     u = (self.__vUp.crossProduct(viewDir))
   #     u.normalize()
        #u.print("u")
        #print(negViewDir)
   #     v = (-viewDir).crossProduct(u)
   #     return [u,v]

    #def getHalf(self):
        #vFovRad = math.radians(self.__vFov)
    #    d = 1
    #    hh = d * math.tan(self.__vFov/2)
    #    hw = self.__aspect * hh / 4
    #    return[hh,hw]

    def getARay(self, u, v, bottomLeftCorner=1):
        
        destination = self.__bottomLeftCorner + self.__width * u + self.__height * v
        ray = Ray.Ray(self.__lookFrom, destination- self.__lookFrom)
        return ray

    def getHeightAndWidth(self):
        return [self.__width,self.__height]

    #def getViewDir(self):
    #    viewDir = (self.__lookAt - self.__lookFrom)
    #    viewDir.normalize()
    #    return viewDir

    #def getLookAt(self, bottomLeftCorner):
    #    halfs = self.getHalf()
    #    vects = self.getUAndV()
    #    value = bottomLeftCorner + (vects[0]*halfs[1]) + (vects[1]*halfs[0])
    #    return value

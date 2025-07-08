class ClosestHit:
    
    def __init__(self, hitPoint, normal, t, sphere):
        self.__hitPoint = hitPoint
        self.__normal = normal
        self.__t = t
        self.__sphere = sphere

    def getNormal(self):
        return self.__normal

    def getSphere(self):
        return self.__sphere

    def getT(self):
        return self.__t

    def getHitPoint(self):
        return self.__hitPoint

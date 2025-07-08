import Vector3d
import math
import Sphere
import ClosestHit
from Constants import *
import Light

class Ray:
    def __init__(self, e, d):
        self.__eye = e
        self.__direction = d

    def getDirection(self):
        return self.__direction

    def getEye(self):
        return self.__eye

    def rayHitsSphere(self, spheres):
        sphereVals = []
        
        for sphere in spheres:
          #NORAMLIZE
          rayDirection = self.getDirection()
          #rayDirection.normalize()
          eye = self.getEye()
          sphereRadius = sphere.getRadius()
          centerVector = sphere.getCenterVector()
          eyeToDist = eye - centerVector
          a = rayDirection.dotProductScalar(rayDirection)
          b = DISCRIM_TWO * ((centerVector - eye).dotProductScalar(rayDirection))
          c = ((eye - centerVector).dotProductScalar(eye - centerVector)) - math.pow(sphereRadius,2)
          discriminant = math.pow(b,2) - DISCRIM_FOUR * a * c
          if discriminant >= 0:
            t = self.getT(sphere)
            hitPoint = self.getPointOnARay(t)
            normal = hitPoint - centerVector
            closestHit = ClosestHit.ClosestHit(hitPoint, normal, t, sphere)
            sphereVals.append([True, closestHit])
          else:
            sphereVals.append([False])
        smallestT = ONE_THOUSAND
        closestHit = 0
        for sphereVal in sphereVals:
            if (sphereVal[0] == True):
              newClosestHit = sphereVal[1]
              newT = newClosestHit.getT()
              if newT < smallestT:
                  closestHit = newClosestHit
                  smallestT = newT
        returnVal = False
        if (closestHit != 0):
          returnVal = [True, closestHit]
        return returnVal

    def getPointOnARay(self, t):
        return self.__eye + (self.__direction * t)

    def getT(self, sphere):
        rayDir = self.getDirection()
        rayDir.normalize()
        centerVector = sphere.getCenterVector()
        sphereRadius = sphere.getRadius()
        eye = self.getEye()
        a = rayDir.dotProductScalar(rayDir)
        b = DISCRIM_TWO * ((centerVector - eye).dotProductScalar(rayDir))
        c = ((eye - centerVector).dotProductScalar(eye - centerVector)) - math.pow(sphereRadius,2)
        t1 = (-b + math.sqrt(math.pow(b,2) - 4 * a * c))/ (2 * a)
        t2 = (-b - math.sqrt(math.pow(b,2) - 4 * a * c) - 4 * a * c)/(2 * a)
        if t1 < t2 and t1 != 0:
          return t1
        else:
          return t2


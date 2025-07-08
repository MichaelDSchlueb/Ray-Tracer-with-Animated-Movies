from Constants import *
import Vector3d
import Ray
import Sphere
import ClosestHit
import math
import random
import Light
import Camera
import Bezier

class Image:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__spheres = []
        self.__lights = []
        self.__camera = 0

    def createScene(self):
        midPath = [Vector3d.Vector3d(-6,0,1),
                   Vector3d.Vector3d(-5.5,1,1),
                   Vector3d.Vector3d(-4.5,1,1),
                   Vector3d.Vector3d(-4,0,1)]
        self.__spheres = [Sphere.Sphere(GROUND_RADIUS, Vector3d.Vector3d(0,GROUND_Y,GROUND_Z), MAGENTA, MAGENTA_ACTIV_KEY,"STRIPE",SHARP,"GLAZED"),
                          Sphere.Sphere(MID_RADIUS, MID_POS, BLUE, BLUE_ACTIV_KEY,0,SMOOTH, "GLAZED"),
                          Sphere.Sphere(SMALL_ONE_RADIUS, SMALL_ONE_POS, RED, RED_ACTIV_KEY,"NONE", SHARP, "GLAZED"),
                          Sphere.Sphere(SMALL_TWO_RADIUS, SMALL_TWO_POS, RED, RED_ACTIV_KEY_TWO,0,SHARP, "GLAZED"),
                          Sphere.Sphere(PIE_RADIUS, PIE_POS, PIE_COLOR, PIE_ACTIV_KEY, "NONE",SMOOTH, "NONE")]
                   
        #self.__objects.append(spheres)
        #create light sources
        self.__lights = [Light.Light(LIGHT_ONE_POSITION, DIFFUSE_INTENSITY, SPECULAR_INTENSITY)]#,
                 #Light.Light(LIGHT_SOURCE_POS_2, DIFFUSE_INTENSITY_TWO, SPECULAR_COLOR_TWO)]
        #self.__lights.append(light)
        self.__camera = Camera.Camera(FOV, (RESOLUTION_WIDTH/RESOLUTION_HEIGHT), Vector3d.Vector3d(0,0,-30),Vector3d.Vector3d(0,0,0), Vector3d.Vector3d(1,0,0))
        #camera look at x was 2

    def runRayTracer(self, u, paths, counter):
        # create a new method to calculate the resolution, width, and height. That would be easier.
        #halfUnits = self.__camera.getHalf()
        z = 0
        #vals = self.__camera.getUAndV() removed so I could just get the height and width like so
        dims = self.__camera.getHeightAndWidth()
        self.__width = dims[0]
        self.__height = dims[1]
        ground = self.__spheres[0]
        pie = self.__spheres[4]
        if counter == 3 or counter == 4:
            self.__spheres[1].move(u, paths[0])
        elif counter == 5:
            self.__spheres[2].move(u, paths[1])
            self.__spheres[3].move(u, paths[2])
        if counter == 7:
          for sphere in self.__spheres:
            if sphere != ground and sphere != pie:
                sphere.adjustRadius(paths[z], u)
                z = z + 1
        else:
          for sphere in self.__spheres:
            if sphere != ground and sphere != pie:
                sphere.move(u, paths[z])
                z = z + 1
        z = 0
        if counter == 6 and u == 0.0:
            self.__spheres[0].setMaterial("CHECKERBOARD")
            self.__spheres[2].setMaterial("STRIPE")
            self.__spheres[3].setMaterial("STRIPE")
              #if sphere.getCenterVector == s
        if counter == 6:
            i = 0
            for sphere in self.__spheres:
                #sphere.getCenterVector().print("Center vector of sphere " + str(i))
                i = i + 1
        colorList = []
        closestHit = ZERO
        # p(3) = (-3,-3,2)
        # p(2) = (-4,-5,2)
        #p(0) = (-3, -3,3)
        #p(1) = (-4,-3, 2)
        # call to create to move the balls with the equation
        totalColor = Vector3d.Vector3d(ZERO,ZERO,ZERO)
        bottomLeft = Vector3d.Vector3d(-(self.__width.getX()/DIVIDER), -(self.__height.getY()/DIVIDER), BOTTOM_LEFT_Z)
        #eyepoint = Vector3d.Vector3d(ZERO,ZERO,ZERO)
        offsetX = 4/RESOLUTION_WIDTH
        offsetY = 2/RESOLUTION_HEIGHT
        #move the sphere with the bezier
        for row in range(RESOLUTION_HEIGHT):
          for col in range(RESOLUTION_WIDTH):
            totalColor = Vector3d.Vector3d(ZERO,ZERO,ZERO)
            for _ in range(NUM_SUBRAYS):
                randomX = random.random() * 2 -1
                randomY = random.random() * 2 -1
                # change this because col is x. row is y
                u = ((row + randomX * offsetX)/RESOLUTION_HEIGHT)
                v = ((col + randomY * offsetY)/RESOLUTION_WIDTH)
                #destVec = Vector3d.Vector3d((bottomLeft.getX() + offsetX * col), (bottomLeft.getY() + offsetY * row), bottomLeft.getZ())
                #destVec.setX(destVec.getX() + randomX * offsetX)
                #destVec.setY(destVec.getY() + randomY * offsetY)
                ray = self.__camera.getARay(u,v)
                #dirVec = destVec - eyepoint
                #ray = Ray.Ray(eyepoint, dirVec)
                color = self.calculatePixelColor(ray, (row/RESOLUTION_HEIGHT), DEPTH_START)
                totalColor = totalColor + color
            totalColor = totalColor * (1/NUM_SUBRAYS)
            colorList.append(totalColor)
          if (row % MODULOUS == ZERO) and (row != 0):
              print("processing row: ", row)
        return colorList

    def calculatePixelColor(self, ray, t, depth):
        if depth == MAX_DEPTH:
              return Vector3d.Vector3d(ZERO,ZERO,ZERO)
        hitObject = ray.rayHitsSphere(self.__spheres)
        #print(hitObject)
        if hitObject:
            ###p = ray.getPointOnARay(hitObject[1].getT())
            if hitObject[1].getSphere().getMaterial() == "STRIPE":
                pixelColor = self.generateStripeTexture(hitObject[1].getHitPoint())
            elif hitObject[1].getSphere().getMaterial() == "CHECKERBOARD":
                pixelColor = self.generateCheckerboardTexture(hitObject[1].getHitPoint())
            else:
                pixelColor = hitObject[1].getSphere().getColor()
            if LIGHT_TYPE == "NONE":
                return pixelColor
            elif LIGHT_TYPE == "FAUX":
              normal = hitObject[1].getNormal()
              normal.normalize()
              color = hitObject[1].getSphere().getColor()
              activKey = hitObject[1].getSphere().getActivationKey()
              xChange = (normal.getX() + ONE)/TWO
              yChange = (normal.getY() + ONE)/TWO
              zChange = (normal.getZ() + ONE)/TWO
              normal.setX(xChange * activKey.getX())
              normal.setY(yChange * activKey.getY())
              normal.setZ(zChange * activKey.getZ())
              normal *= COLOR_MAX
              if normal.getZ() >= TWO_HUNDRED:
                  normal.setZ(TWO_HUNDRED)
              return normal #+ finalColor
            elif LIGHT_TYPE == "BLINN-PHONG":
               result = pixelColor
               #if hitObject[1].getSphere().getReflectionType() == "GLAZED":
                  #print("HERE")
                  #normal = hitObject[1].getNormal()
                  #normal.normalize()
                  #d = ray.getDirection()
                  #d.normalize()
                  #r = d - normal * 2*(d.dotProductScalar(normal))
                  #if fuzziness != 0:
                    # r = r + closestHit.getFuzziness()*randomValueFromUnitCube()
                  #p = hitObject[1].getHitPoint()
                  #specReflectRay = Ray.Ray(p, r)
                  #closestSRefHit = specReflectRay.rayHitsSphere(self.__spheres[0])
                  #if closestSRefHit:
                  #    result = closestSRefHit[1].getSphere().getColor() + self.calculatePixelColor(specReflectRay, t, depth+1) 
               pixelColor = self.calculateBlinnPhongShading(ray, hitObject[1], result)
               #pixelColor.print("pixelColor")
               #shadow = self.calculateShadows(hitObject[1],p)
               #pixelColor.print("pixelColor")
               #pixelColor = pixelColor# * shadow
               #pixelColor.print("finalColor")
               pixelColor.clamp()
               #pixelColor.print("pixelColor")
               return pixelColor
        else:
            unitDir = ray.getDirection()
            unitDir.normalize()
            pixelColor = BLUE*(.9-t) + WHITE*(t + .1)
            return pixelColor

    def calculateBlinnPhongShading(self, ray, closestHit, curPixelColor):
        ambient = curPixelColor * AMBIENT_INTENSITY
        diffuse = Vector3d.Vector3d(0,0,0)
        specular = Vector3d.Vector3d(0,0,0)
        for light in self.__lights:
          v = ray.getEye() - closestHit.getHitPoint()
          v.normalize()
          v = -1 * v
          l = closestHit.getHitPoint() - light.getPosition()
          l.normalize()
          h = v + l
          h.normalize()
          n = closestHit.getNormal()
          n.normalize()
          #l.print("L")
          diffuse += curPixelColor * light.getDiffuse() * max(0.0, n.dotProductScalar(l))
          #v.print("v")
          #h.print("h")
          specular += curPixelColor * light.getSpecular() * (max(0.0, n.dotProductScalar(h))**200)
        #ambient is independent
        #print("diffuse ", light.getDiffuse())
        #print("specular ", light.getSpecular())
        #n.print("n")
        #l.print("l")
        #closestHit.getHitPoint().print("hit point ")
        #print("dot product ", n.dotProductScalar(l))
        #ambient.print("ambient")
        #diffuse.print("diffuse")
        #specular.print("specular")
        shadingResult = ambient + diffuse + specular
        #shadingResult.clamp()
        final = curPixelColor + shadingResult
        #shadingResult.print("shadingResult")
        return final
        
    def calculateShadows(self, closestHit,p):
      numberOfRaysHit = 0
      for lights in self.__lights[0]:
        for _ in range(NUM_SHADOW_RAYS):
          l = lights.getPosition() - closestHit.getHitPoint()
          l.normalize()
          #norm = closestHit.getNormal()
          #norm.normalize()
          if NUM_SHADOW_RAYS > 1 and closestHit.getSphere().getShadowType != "SHARP":
            offset = random.random() * 0.5
            l.setX(l.getX() + offset)
            l.setY(l.getY() + offset)
            l.setZ(l.getZ() + offset)
          shadowRay = Ray.Ray(p * .0000000001, l)
          shadowHit = shadowRay.rayHitsSphere(self.__spheres)
          if shadowHit:
              numberOfRaysHit += 1
      shadowPercentage = numberOfRaysHit/NUM_SHADOW_RAYS  
      if shadowHit:
        if closestHit.getSphere().getShadowType() == "SHARP":
          #print("HERE")
          return 0.7
        elif closestHit.getSphere().getShadowType() == "SMOOTH":
            #print("HI!")
            return shadowPercentage * 0.5
            #print("FALSE")
      else:
           return 1

    def generateStripeTexture(self, hitPoint):
        a = .25
        b = 0
        x = hitPoint.getX()
        if math.sin(a * x + b) > 0:
             #print(a * x + b)
             return Vector3d.Vector3d(255,255,0)
        else:
            return Vector3d.Vector3d(255,ZERO,255)

    def generateCheckerboardTexture(self, hitPoint):
        a1 = 0.25
        a2 = 0.25
        x = hitPoint.getX()
        y = hitPoint.getY()
        b1 = 0
        b2 = 0
        if (math.sin(a1 * x + b1) > 0) ^ (math.sin(a2 * y + b2) > 0):
            return Vector3d.Vector3d(255,255,255)
        else:
            return Vector3d.Vector3d(255,0,0)


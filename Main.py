import Image
from Constants import *
import Vector3d
import time
import random
from PIL import Image as Img
import os
#import Bezier

class Main:

    def run(self):

        image = Image.Image(WIDTH, HEIGHT)
        frameNum = 1
        u = 0.0
        z = 0
        i = 1
        mainAnimPause = 0
        checkedOff = False
        counter = 0
        mainAnimStopped = False
        image.createScene()
        #random.seed(
        paths = [MID_PATH,SMALL_ONE_PATH, SMALL_TWO_PATH]
        upIndicator = False
        fallBackIndicator = False
        #midPath = [Vector3d.Vector3d(-6,0,1),
        #           Vector3d.Vector3d(-5.5,1,1),
        #           Vector3d.Vector3d(-4.5,1,1),
        #           Vector3d.Vector3d(-4,0,1)]
        #paths.append(midPath)
        #small_one_path = [
        for _ in range(NUM_FRAMES):
          print("Now commencing with frame #", frameNum)
          start = time.time()
          colors = image.runRayTracer(u, paths,counter)
          end = time.time()
          total = end - start
        #ppm = ppmRender.ppmRender()
          self.generate(colors, total, frameNum)
          if fallBackIndicator:
              u = u - 0.1
          else:
              u = u + 0.1
              u = float(u)
          print("u = " + str(u))
          #if u > 1.09 and z != 3
          if u < 0.0:
              fallBackIndicator = False
              #upIndicator = False
          if u > 0.9999999999999999 or u < 0.000000000004:
              #something here so we can indicate that it's time for it to come crashing down
            if upIndicator and u == 1.0999999999999999:
                fallBackIndicator = True
            if fallBackIndicator:
                u = u - 0.1
                if counter == 6 or counter == 7 or counter == 8:
                    checkedOff = False
            else:
             u = 0
             fallBackIndicator = False
             counter = counter + 1
             print(counter)
            if counter == 3 and checkedOff == False:
               #print("NO!")
            #change ht ebezier points for the purpose of jumping up
               mainAnimPause = paths
               mainAnimStopped = True
               paths[0] = MID_JUMP
               paths[1] = SMALL_ONE_JUMP
               paths[2] = SMALL_TWO_JUMP
               upIndicator = True
               checkedOff = True
            #elif counter == 4 and checkedOff == True:
               #upIndicator = True
            if counter == 6:
               #print("Fixed")
               paths[0] = MID_FORWARD_PATH
               paths[1] = SMALL_ONE_PATH_FORWARD
               paths[2] = SMALL_TWO_PATH_FORWARD
               checkedOff = True
            if counter == 7:
               #print("unrecognized")
               paths[0] = RADIUS_STRETCH
               paths[1] = SMALL_ONE_STRETCH
               paths[2] = SMALL_TWO_STRETCH
               #print("radius val 1", paths[0])
               #print("radius val 2", paths[1])
               #print("radius val 3", paths[2])
               checkedOff = True
            if counter == 8:
                mainAnimStopped = False
                paths[0] = mainAnimPause[0]
                paths[1] = mainAnimPause[1]
                paths[2] = mainAnimPause[2]
                #paths[3] = mainAnimPause[3]
           # if counter > 3 or counter < 7:
           #     upIndicator = True
            if mainAnimStopped == False:
                 for path in paths:
                 #  print("JUMP #" + str(counter) + " completed")
                   #for controlPoint in path:
                      #controlPoint.print("Control Point " + str(i) + " before")
                #    i = i + 1
                #    i = 0
                   path[0].setX(path[0].getX() + 2)
                   path[1].setX(path[1].getX() + 2)
                   path[2].setX(path[2].getX() + 2)
                   path[3].setX(path[3].getX() + 2)
                   u = 0
                   #for controlPoint in path:
                   #  controlPoint.print("Control Point " + str(i) + " after")
                   #  i = i + 1
                   #  i = 0
                #counter =  counter + 1
          frameNum = frameNum + 1
        print("Your movie frames are rendered")

    def generate(self, rgbTuples, totalTime, frameNum):
    #new path but with different folder name
          path = os.path.join("Output Frames", "frame_"+ str(RESOLUTION_WIDTH) + "x" + str(RESOLUTION_HEIGHT) + "_00" + str(frameNum) + ".ppm")
          path2 = os.path.join("Output Frames/Output PNGs", "frame_"+ str(RESOLUTION_WIDTH) + "x" + str(RESOLUTION_HEIGHT) + "_00" + str(frameNum) + ".png")
          f = open(path, "w")
          f.write("P3\n")
          for pixel in rgbTuples:
            pixel.clamp()
          f.write(str(RESOLUTION_WIDTH) + " " + str(RESOLUTION_HEIGHT) + "\n")
          f.write("255\n")
          i = ZERO 
          for row in range(RESOLUTION_HEIGHT):
              for col in range(RESOLUTION_WIDTH):
                  f.write(str(int(rgbTuples[i].getX())) + " " + str(int(rgbTuples[i].getY())) + " " + str(int(rgbTuples[i].getZ())) + "\n")
                  i = i + INCREMENT
          f.close()
          #path2 = os.path.join("Output PNGs", "frame_"+ str(RESOLUTION_WIDTH) + "x" + str(RESOLUTION_HEIGHT) + "_00" + str(frameNum) + "_" + str(int(totalTime)) + "s.png")
          im = Img.open(path)
          im.save(path2)
          #print("finished frame " + str(frameNum))
        

def main():
    main = Main()
    main.run()

main()

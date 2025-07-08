from Constants import *
import os
import Vector3d
from PIL import Image as Img

class ppmRender:

  def generate(self, rgbTuples, totalTime, frameNum):
          path = os.path.join("Output Frames", "frame_"+ str(RESOLUTION_WIDTH) + "x" + str(RESOLUTION_HEIGHT) + "_00" + str(frameNum) + "_" + str(int(totalTime)) + "s.ppm")
          path2 = os.path.join("Output PNGs", "frame_"+ str(RESOLUTION_WIDTH) + "x" + str(RESOLUTION_HEIGHT) + "_00" + str(frameNum) + "_" + str(int(totalTime)) + "s.png")
          f = open(path, "w")
          f.write("P3\n")
          for two in rgbTuples:
            two.clamp()
          f.write(str(RESOLUTION_WIDTH) + " " + str(RESOLUTION_HEIGHT) + "\n")
          f.write("255\n")
          i = ZERO 
          for row in range(RESOLUTION_HEIGHT):
              for col in range(RESOLUTION_WIDTH):
                  f.write(str(int(rgbTuples[i].getX())) + " " + str(int(rgbTuples[i].getY())) + " " + str(int(rgbTuples[i].getZ())) + "\n")
                  i = i + INCREMENT
          f.close()
          im = Img.open(path)
          im.save(path2)
          print("finished frame " + str(frameNum))


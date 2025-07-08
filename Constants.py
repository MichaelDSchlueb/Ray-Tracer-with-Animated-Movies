import Vector3d

VEC_X_CORD = 20
VEC_Y_CORD = 90
VEC_Z_CORD = 80
VEC2_X_CORD = -20
VEC2_Y_CORD = -90
VEC2_Z_CORD = -80
MULT_FACTOR = 70
NEW_COORD_X = 100
NEW_COORD_Y = 12
NEW_COORD_Z = 80
RESOLUTION_HEIGHT = 150
RESOLUTION_WIDTH = 300
WIDTH = 4
HEIGHT = 2
Z_VALUE_BOTTOM_LEFT = -1
Z_VALUE_SPHERE = 1
MODULOUS = 10
COLOR_MAX = 255
DISCRIM_FOUR = 4
SPHERE_RADIUS = 0.5
SPHERE_POS_X = 0
SPHERE_POS_Y = 0
SPHERE_POS_Z = 0
#No using decimals
MID_POS = Vector3d.Vector3d(-6,0,1)
SMALL_ONE_POS = Vector3d.Vector3d(-5,-1,1)
SMALL_TWO_POS = Vector3d.Vector3d(-7,-1,1)
SEED_VALUE = 10
MID_PATH = [Vector3d.Vector3d(-6,0,1),
            Vector3d.Vector3d(-6,1,1),
            Vector3d.Vector3d(-4,1,1),
            Vector3d.Vector3d(-4,0,1)]

SMALL_ONE_PATH = [Vector3d.Vector3d(-5,-1,1),
                  Vector3d.Vector3d(-5,0,1),
                  Vector3d.Vector3d(-3,0,1),
                  Vector3d.Vector3d(-3,-1,1)]

SMALL_TWO_PATH = [Vector3d.Vector3d(-7,-1,1),
                  Vector3d.Vector3d(-7,0,1),
                  Vector3d.Vector3d(-5,0,1),
                  Vector3d.Vector3d(-5,-1,1)]

MID_FORWARD_PATH = [Vector3d.Vector3d(0,0,1),
                    Vector3d.Vector3d(0,1,1),
                    Vector3d.Vector3d(0,1,3),
                    Vector3d.Vector3d(0,0,3)]

SMALL_ONE_PATH_FORWARD = [Vector3d.Vector3d(1,-1,1),
                          Vector3d.Vector3d(1,0,1),
                          Vector3d.Vector3d(1,0,3),
                          Vector3d.Vector3d(1,-1,3)]

SMALL_TWO_PATH_FORWARD = [Vector3d.Vector3d(-1,-1,1),
                          Vector3d.Vector3d(-1,0,1),
                          Vector3d.Vector3d(-1,0,3),
                          Vector3d.Vector3d(-1,-1,3)]

CAMERA_PAN = [Vector3d.Vector3d(0,0,-30),
              Vector3d.Vector3d(0,1,-30),
              Vector3d.Vector3d(0,2,-30),
              Vector3d.Vector3d(0,3,-30)]

RADIUS_STRETCH = [0.5, 0.75, 0.86, 1]

SMALL_ONE_STRETCH = [0.2,0.6,0.8,1]

SMALL_TWO_STRETCH = [0.19,0.6,0.8,1]
                          
#P_0 = (-3,-2,4)
P_1 = Vector3d.Vector3d(-4,-2,3)
P_2 = Vector3d.Vector3d(-4,-4,3)
P_3 = Vector3d.Vector3d(-3,-2,3)
# p(3) = (-3,-3,2)
        # p(2) = (-4,-5,2)
        #p(0) = (-3, -3,3)
        #p(1) = (-4,-3, 2)
# radius will be 0.1
# will need to increase radius
#P(0.5) = (0, 1.5, -2)
# p(1) = (-0.5, 1.5, -1.5)
PLOT_2 = Vector3d.Vector3d(-0.5, 1.5, -1.5)
MID_JUMP = [Vector3d.Vector3d(0,0,1),
            Vector3d.Vector3d(0,0.5,0),
            Vector3d.Vector3d(0,1,0),
            Vector3d.Vector3d(0,1.5,0)]

SMALL_ONE_JUMP = [Vector3d.Vector3d(1,-1,1),
                  Vector3d.Vector3d(1,0,1),
                  Vector3d.Vector3d(1,2,1),
                  Vector3d.Vector3d(1,4,1)]

SMALL_TWO_JUMP = [Vector3d.Vector3d(-1,-1,1),
                  Vector3d.Vector3d(-1,0,1),
                  Vector3d.Vector3d(-1,2,1),
                  Vector3d.Vector3d(-1,4,1)]
#self.__point1 = point1
        #self.__point1.print("p1")
 #       self.__point2 = point2
        #self.__point2 = self.shift2()
        #self.__point2.print("p2")
  #      self.__point3 = point4
        #self.__point3 = self.shift3()
        #self.__point3.print("p3")
   #     point2.setY(point2.getY() -4)
    #    self.__point4 = point2
        #self.shift4()
     #   point3.set(point3.getZ() + 1)
      #  self.__point5 = point3
      #  point4.setY(point4.getY() - 10)
      #  self.__point6 = point4
        #self.__point4.print("p4")
       # point3.setZ(point3.getZ()-2)
       # self.__point7 = point3
DIVIDER = 2
BOTTOM_LEFT_Z = -1
INCREMENT = 1
ZERO = 0
DISCRIM_TWO = 2
FRAME_START = 1
NUM_SUBRAYS = 2
MULT_FACTOR_FOR_BLUE = 40
ORANGE = Vector3d.Vector3d(252,164,0)
LIGHT_TYPE = "BLINN-PHONG"
MAGENTA = Vector3d.Vector3d(255,1,255)
MAGENTA_ACTIV_KEY = Vector3d.Vector3d(1,0,1)
BLUE = Vector3d.Vector3d(0,0,255)
BLUE_ACTIV_KEY = Vector3d.Vector3d(0,0,15)
WHITE = Vector3d.Vector3d(255,255,255)
RED = Vector3d.Vector3d(100,0,0)
RED_ACTIV_KEY = Vector3d.Vector3d(4,0,0)
RED_ACTIV_KEY_TWO = Vector3d.Vector3d(1,0,0)
PIE_RADIUS = 0.3
PIE_COLOR = Vector3d.Vector3d(150,105,25)
PIE_ACTIV_KEY = Vector3d.Vector3d(1.7,2.4,10.2)
PIE_POS = Vector3d.Vector3d(0,-3,3)
MID_RADIUS = 0.5
SMALL_ONE_RADIUS = 0.2
SMALL_ONE_X = 0.7
SMALL_Y = -0.35
SMALL_ONE_Z = 0.9
SMALL_TWO_RADIUS = 0.19
SMALL_TWO_X = -0.7
SMALL_TWO_Z = 0.85
GROUND_RADIUS = 50
GROUND_Y = -50
GROUND_Z = 0
ONE = 1
TWO = 2
TWO_HUNDRED = 200
ONE_THOUSAND = 1000
LIGHT_SOURCE_ONE_AMBIENT_COLOR = Vector3d.Vector3d(255,255,0)
AMBIENT_INTENSITY = 0.1
LIGHT_SOURCE_ONE_DIFFUSE_COLOR = Vector3d.Vector3d(255,0,255)
DIFFUSE_INTENSITY = 0.7
LIGHT_SOURCE_ONE_SPECULAR_COLOR = Vector3d.Vector3d(0,255,255)
SPECULAR_INTENSITY = 0.9
LIGHT_SOURCE_TWO_AMBIENT_COLOR = Vector3d.Vector3d(0,0,255)
AMBIENT_INTENSITY_TWO = .15
LIGHT_SOURCE_TWO_DIFFUSE_COLOR = Vector3d.Vector3d(0,255,0)
DIFFUSE_INTENSITY_TWO = 0.43
LIGHT_SOURCE_TWO_SPECULAR_COLOR = Vector3d.Vector3d(255,0,0)
SPECULAR_COLOR_TWO = .20
P = 5
LIGHT_ONE_POSITION = Vector3d.Vector3d(0, 2, -9)
# origianl was 1, -3,2
SHARP = "SHARP"
SMOOTH = "SMOOTH"
MAX_DEPTH = 1
DEPTH_START = 0
NUM_SHADOW_RAYS = 1
LIGHT_SOURCE_POS_2 = Vector3d.Vector3d(0.5, 0.2, 8)
FOV = 15
NEGATE_FACTOR = -1
NUM_FRAMES = 144

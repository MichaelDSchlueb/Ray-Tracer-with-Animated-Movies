from Vector3d import *
from Constants import *

def main():
    vec = Vector3d(VEC_X_CORD,VEC_Y_CORD,VEC_Z_CORD)
    vec.print("The following vector 1 is")    

    print("The x in vec is ", vec.getX())

    print("The y in vec is ", vec.getY())

    print("The z in vec is ", vec.getZ())
    
    vec2 = Vector3d(VEC2_X_CORD,VEC2_Y_CORD,VEC2_Z_CORD)

    vec2.print("The following vector 2 is")

    subVector = vec - vec2
    subVector.print("vec and vec2 are subtracted as follows ")

    multVec = vec * MULT_FACTOR
    multVec.print("vec is multiplied by a scalar ")

    print("The distance of the following vector between vec and vec2 is: ", vec.distance(vec2))

    print("The dot product of vec and vec2 is as follows : ", vec.dotProductScalar(vec2))

    print("The angle between the dot product of vec and vec2 is as follows: ", vec.dotProductAngle(vec2))

    print("The length of vec is ", vec.length())
    
    vec.normalize()
    print("vec 1 is normalized as follows: ", vec.getX(), vec.getY(), vec.getZ())

    addVec = vec + vec2
    addVec.print("vec and vec2 are added like so ")

    vec.setX(NEW_COORD_X)
    print("vec x is now ", vec.getX())
    vec.setY(NEW_COORD_Y)
    print("vec y is now ", vec.getY())
    vec.setZ(NEW_COORD_Z)
    print("vec z is now ", vec.getZ())
    vec2 = -vec


    vec2.print("Negated form of vec2 is")

main()

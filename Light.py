class Light:

    def __init__(self, position, diffuse, specular):
        self.__position = position
        self.__diffuse = diffuse
        self.__specular = specular

    def getDiffuse(self):
        return self.__diffuse

    def getPosition(self):
        return self.__position

    def getSpecular(self):
        return self.__specular

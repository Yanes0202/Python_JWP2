import math


class Vector3D:
    def __init__(self, x, y, z):
        self.__x__ = x
        self.__y__ = y
        self.__z__ = z

    def __str__(self):
        return f"Vector3D({self.__x__}, {self.__y__}, {self.__z__})"

    def __add__(self, other):
        return Vector3D(self.__x__ + other.__x__, self.__y__ + other.__y__, self.__z__ + other.__z__)

    def __sub__(self, other):
        return Vector3D(self.__x__ - other.__x__, self.__y__ - other.__y__, self.__z__ - other.__z__)

    def __mul__(self, other):
        return Vector3D(self.__x__ * other, self.__y__ * other, self.__z__ * other)

    def dot(self, other):
        return self.__x__ * other.__x__ + self.__y__ * other.__y__ + self.__z__ * other.__z__

    def cross(self, other):
        return Vector3D(self.__y__ * other.__z__ - self.__z__ * other.__y__,
                        self.__z__ * other.__z__ - self.__x__ * other.__z__,
                        self.__x__ * other.__y__ - self.__y__ * other.__x__)

    def are_orthogonal(self, other):
        return Vector3D.dot(self, other) == 0

    def getX(self):
        print(self.__x__)

    def setX(self, x):
        self.__x__ = x

    def getY(self):
        print(self.__y__)

    def setY(self, y):
        self.__y__ = y

    def getZ(self):
        print(self.__z__)

    def setZ(self, z):
        self.__z__ = z

    def przesun(self, x, y, z):
        self.__x__ += x
        self.__y__ += y
        self.__z__ += z

    def norm(self):
        return math.sqrt(math.pow(self.__x__, 2) + math.pow(self.__y__, 2) + math.pow(self.__z__, 2))

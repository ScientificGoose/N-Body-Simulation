from vector.Vector import Vector
from math import sqrt
from math import pow

class Vector3D(Vector):

    def __init__(self, x=0.0, y=0.0, z=0.0):

        if(isinstance(x, float) and isinstance(y, float) and isinstance(z, float)):
            self._x = x
            self._y = y
            self._z = z

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def add(self, vector=None, x=0.0, y=0.0, z=0.0):
        """
        This method adds two Vector3D objects together.

        Parameters
        ----------
        vector (Vector3D): The vector to be added to the current object.
        x (float): The x coordinate.
        y (float): The y coordinate.
        z (float): The z coordinate.
        """
        if(vector and isinstance(vector, Vector3D)):
            self.x += vector.x
            self.y += vector.y
            self.z += vector.z
        elif(isinstance(x, float), isinstance(y, float), isinstance(z, float)):
            self.x += x
            self.y += y
            self.z += z
        else:
            print("You cannot add two vectors of different dimensions!")


    def get_difference_vector(self, vector):
        """
        This method will calculate the difference between two Vectors and return the resulting vector.

        Parameters
        ----------
        vector (Vector3D): The Vector to be compared to this object.

        return (Vector3D): The resulting Vector3D object.
        """
        if isinstance(vector, Vector3D):
            temp_vector = Vector3D()
            temp_vector.x = vector.x - self.x
            temp_vector.y = vector.y - self.y
            temp_vector.z = vector.z - self.z
        else:
            raise ValueError("This cannot be performed on vectors of different dimensions!")

        return temp_vector

    def get_distance_to(self, vector):
        """
        This method returns the distance between two Vector2D objects.
        distance(a, b, c)(a, b, c) = sqrt((a - a)^2 + (b - b)^2 + (c - c)^2)
        
        Parameters
        ----------
        vector (Vector3D): The Vector2D object to calculate the distance from.

        return: A float value of the distance between the two vectors.
        """
        if isinstance(vector, Vector3D):
            return sqrt(
                pow(self.x - vector.x, 2) +
                pow(self.y - vector.y, 2) +
                pow(self.z - vector.z, 2)
                )

    def update(self, vector=None, x=0.0, y=0.0, z=0.0):
        """
        This method will change the coordinates of a the Vector.

        Parameters
        ----------
        vector (Vector2D): A tuple with the coordinates to update to.

        x (float): The x value for the vector.

        y (float): The y value for the vector.

        z (float): The z value for the vector.
        """

        if(vector and isinstance(vector, Vector3D)):
            self.x = vector.x
            self.y = vector.y
            self.z = vector.z
        elif(isinstance(x, float) and isinstance(y, float) and isinstance(z, float)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError("Invalid input!")

    def apply_scalar(self, scalar):
        """
        This method will apply an input scalar to the vector.

        Parameters
        ----------
        scalar (float): The scalar to be applied to the Vector.
        """
        if isinstance(scalar, float):
            self.x *= scalar
            self.y *= scalar
            self.z *= scalar
        else:
            raise ValueError(f"{scalar} is not a float!")

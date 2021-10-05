from vector.Vector import Vector
from math import sqrt
from math import pow

class Vector3D(Vector):

    def __init__(self, x=0.0, y=0.0, z=0.0):

        if(isinstance(x, float) and isinstance(y, float) and isinstance(z, float)):
            self.x = x
            self.y = y
            self.z = z

    @property
    def get_x(self) -> float:
        return self.x

    @property
    def get_y(self) -> float:
        return self.y

    @property
    def get_z(self) -> float:
        return self.z

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
            self.x += vector.get_x
            self.y += vector.get_y
            self.z += vector.get_z
        elif(isinstance(x, float), isinstance(y, float), isinstance(z, float)):
            self.x += x
            self.y += y
            self.z += z
        else:
            print("You cannot add two vectors of different dimensions!")

    def get_distance_between(self, vector):
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
                pow(self.x - vector.get_x, 2) +
                pow(self.y - vector.get_y, 2) +
                pow(self.z - vector.get_z, 2)
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
            self.x = vector.get_x
            self.y = vector.get_y
            self.z = vector.get_z
        elif(isinstance(x, float) and isinstance(y, float) and isinstance(z, float)):
            self.x = x
            self.y = y
            self.z = z

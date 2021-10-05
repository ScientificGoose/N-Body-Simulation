from vector.Vector import Vector
from math import sqrt
from math import pow


class Vector2D(Vector):
    """

    This class represents a 2 dimensional vector.

    Methods
    -------

    __init___(x=0.0, y=0.0)
        This is the default constructor.
    """

    def __init__(self, x=0.0, y=0.0):
        """
        This is the constructor for the Vector 2D class.

        Parameters
        ----------
        x (float): The x position of the vector.
        y (float): The y position of the vector.

        """

        if(isinstance(x, float) and isinstance(y, float)):
            self.x = x
            self.y = y

    @property
    def get_x(self) -> float:
        return self.x

    @property
    def get_y(self) -> float:
        return self.y

    def add(self, vector=None, x=0.0, y=0.0):
        """
        This method adds two Vector2D objects together.

        Parameters
        ----------
        vector (Vector2D): A Vector2D object to be added to this object.
        x (float): The x coordinate.
        y (float): The y coordinate.
        """

        if(vector and isinstance(vector, Vector2D)):
            self.x += vector.get_x
            self.y += vector.get_y
        elif(isinstance(x, float) and isinstance(y, float)):
            self.x += x
            self.y += y
        else:
            print("You cannot add two vectors of different dimensions!")

    def get_distance_between(self, vector) -> float:
        """
        This method returns the distance between two Vector2D objects.
        distance(a, b)(a, b) = sqrt((a - a)^2 + (b - b)^2)
        
        Parameters
        ----------
        vector (Vector2D): The Vector2D object to calculate the distance from.

        return: A float value of the distance between the two vectors.
        """
        if isinstance(vector, Vector2D):
            return sqrt(
                pow(self.x - vector.get_x, 2) + 
                pow(self.y - vector.get_y, 2)
                )

    def update(self, vector=None, x=0.0, y=0.0):
        """
        This method will change the coordinates of a the Vector.

        Parameters
        ----------
        vector (Vector2D): A tuple with the coordinates to update to.

        x (float): The x value for the vector.

        y (float): The y value for the vector.
        """

        if(vector and isinstance(vector, Vector2D)):
            self.x = vector.get_x
            self.y = vector.get_y
        elif(isinstance(x, float) and isinstance(y, float)):
            self.x = x
            self.y = y

from .vector import Vector
from math import sqrt, pow


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
            self._x = x
            self._y = y

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
            self.x += vector.x
            self.y += vector.y
        elif(isinstance(x, float) and isinstance(y, float)):
            self.x += x
            self.y += y
        else:
            raise ValueError("You cannot add two vectors of different dimensions!")

    def get_difference_vector(self, vector):
        """
        This method will calculate the difference between two Vectors and return the resulting vector.

        Parameters
        ----------
        vector (Vector2D): The Vector to be compared to this object.

        return (Vector2D): The resulting Vector3D object.
        """
        if isinstance(vector, Vector2D):
            temp_vector = Vector2D()
            temp_vector.x = vector.x - self.x
            temp_vector.y = vector.y - self.y
        else:
            raise ValueError("This cannot be performed on vectors of different dimensions!")

        return temp_vector

    def get_distance_to(self, vector) -> float:
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
                pow(vector.x - self.x, 2) + 
                pow(vector.y - self.y, 2)
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
            self.x = vector.x
            self.y = vector.y
        elif(isinstance(x, float) and isinstance(y, float)):
            self.x = x
            self.y = y
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
        else:
            raise ValueError(f"{scalar} is not a float!")

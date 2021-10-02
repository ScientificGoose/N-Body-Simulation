from vector.Vector import Vector
from math import sqrt
from math import pow


class Vector2D(Vector):

    def __init__(self, x, y):
        """
        This is the constructor for the Vector 2D class.
        :param x: A float for the x position.
        :param y: A float for the y position.
        """
        if isinstance(x, float):
            self.x = x
        if isinstance(y, float):
            self.y = y

    @property
    def get_x(self):
        return self.x

    def set_x(self, x):
        """
        :param x: A float for the new x position.
        """
        if isinstance(x, float):
            self.x = x

    @property
    def get_y(self):
        return self.y

    def set_y(self, y):
        """

        :param y: A float for the new y position.
        """
        self.y = y

    def add_vector(self, vector):
        """
        This method adds two Vector2D objects together.
        :param vector: A Vector2D object to be added to this object.
        """
        if isinstance(vector, Vector2D):
            self.x += vector.get_x
            self.y += vector.get_y

        else:
            print("You cannot add two vectors of different dimensions!")

    def get_distance_between(self, vector: Vector) -> float:
        """
        This method returns the distance between two Vector2D objects.
        distance(a, b)(a, b) = sqrt((a - a)^2 + (b - b)^2

        :param vector: The Vector2D object to calculate the distance from.
        :return: A float value of the distance between the two vectors.
        """
        if isinstance(vector, Vector2D):
            return sqrt(pow(self.x - vector.get_x, 2) + pow(self.y - vector.get_y, 2))

    def apply_scalar(self, scalar):

        if isinstance(scalar, float):
            self.x = self.x * scalar
            self.y = self.y * scalar

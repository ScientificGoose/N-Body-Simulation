from abc import ABC, abstractmethod


class Vector(ABC):
    """
    This is the abstract class for the Vector package

    ...

    Abstract Methods
    -------
    add(vector)
        Adds an input vector to the Vector object.

    distance_to(vector) -> float
        Calculates the distance between the two vector objects.

    """

    distance_to(vector) -> Vector:

    @abstractmethod
    def add(self, vector):
        pass

    @abstractmethod
    def distance_to(self, vector) -> float:
        pass

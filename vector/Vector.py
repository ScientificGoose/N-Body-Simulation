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

    update(vector)
        This is to manually set the vectors values.

    """

    @abstractmethod
    def add(self, vector):
        pass

    @abstractmethod
    def get_distance_between(self, vector) -> float:
        pass

    @abstractmethod
    def update(self, vector):
        pass

from abc import ABC, abstractmethod


class Vector(ABC):

    @abstractmethod
    def add_vector(self, vector):
        pass

    @abstractmethod
    def get_distance_between(self, vector):
        pass

    @abstractmethod
    def apply_scalar(self, scalar):
        pass

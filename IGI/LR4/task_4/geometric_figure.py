from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    """Abstract class of geometric figure."""

    @abstractmethod
    def calculateS(self):
        pass

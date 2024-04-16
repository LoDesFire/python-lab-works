import pickle
from . import FracCollection


class PickleSerializer:
    """Wrapper for pickle"""
    def __init__(self, path):
        self.__path = path

    def save(self, frac_collection: FracCollection):
        """Save FraCollection into the file"""
        with open(self.__path, "wb+") as file:
            pickle.dump(frac_collection, file)

    def obtain(self) -> FracCollection:
        """Obtain FraCollection from the file"""
        with open(self.__path, "rb") as file:
            return pickle.load(file)

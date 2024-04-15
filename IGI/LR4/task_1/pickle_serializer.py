import pickle
from task_1 import FracCollection


class PickleSerializer:
    def __init__(self, path):
        self.__path = path

    def save(self, frac_collection: FracCollection):
        with open(self.__path, "wb+") as file:
            pickle.dump(frac_collection, file)

    def obtain(self) -> FracCollection:
        with open(self.__path, "rb") as file:
            return pickle.load(file)

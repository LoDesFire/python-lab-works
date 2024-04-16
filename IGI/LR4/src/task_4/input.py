from typing import Callable


class Input:
    @staticmethod
    def input_with_checking(_type: type, phrase: str, checker: Callable[[type], bool] = None):
        """Auxiliary function for input checking"""
        while True:
            try:
                res = _type(input(phrase))
                if checker is None or checker(res):
                    return res
                raise ValueError
            except ValueError:
                print("Try again...\n")
from typing import Callable


class Input:
    @staticmethod
    def input_with_checking(_type: type, phrase: str, checker: Callable[[type], bool] = None):
        while True:
            try:
                res = _type(input(phrase))
                if checker is None or checker(res):
                    return res
                raise ValueError
            except ValueError:
                print("Попробуй заново...\n")
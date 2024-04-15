from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Fraction:
    numerator: int
    denominator: int

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __hash__(self):
        return self.__str__().__hash__()


class FracCollection:
    def __init__(self, dictionary: Dict[str, Fraction]):
        self.__dictionary = dictionary

    def __getitem__(self, item):
        return self.__dictionary[item]

    def sorted(self, reverse: bool = False):
        for key in sorted(self.__dictionary.keys(), key=lambda k: float(self.__dictionary[k]), reverse=reverse):
            yield key, self.__dictionary[key]

    def max(self):
        return self.sorted(reverse=True).__next__()

    def find_equals(self):
        keys = set()
        eqls: Dict[float, List[tuple[str, Fraction]]] = dict()

        for k, v in self.__dictionary.items():
            if eqls.get(float(v), None) is not None:
                eqls[float(v)].append((k, v))
                keys.add(float(v))
                continue

            eqls[float(v)] = [(k, v)]

        return [eqls[k] for k in keys]

    def find(self, frac: Fraction) -> str | None:
        for k, v in self.__dictionary.items():
            if float(v) == float(frac):
                return k

        return None

    def to_csv_list(self):
        csv_list = []
        for k, v in self.__dictionary.items():
            csv_list.append({"key": k, "numerator": v.numerator, "denominator": v.denominator})

        return csv_list

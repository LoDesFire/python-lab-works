from .input import Input
from .fraction import Fraction, FracCollection


class Report(Input):

    @classmethod
    def input_frac(cls):
        nominator = cls._input_with_checking(int, "Введите числитель дроби: ")
        denominator = cls._input_with_checking(int, "Введите знаменатель дроби: ")

        frac = Fraction(nominator, denominator)
        return frac

    @classmethod
    def make(cls, fractions: FracCollection, f: Fraction):
        print(f"\nПроверяем число: {f}")
        cls.__relation_report(fractions, f)
        cls.__similars_report(fractions, f)

    @staticmethod
    def __relation_report(fractions: FracCollection, f: Fraction):
        max_fr = fractions.max()[1]
        if float(f) > float(max_fr):
            relation_string = "больше"
        elif float(f) == float(max_fr):
            relation_string = "равно"
        else:
            relation_string = "меньше"
        print(f"Введенное число {relation_string} максимального в словаре")

    @staticmethod
    def __similars_report(fractions: FracCollection, f: Fraction):
        equals_list = fractions.find_equals()

        similar_fracs = None
        for equals in equals_list:
            if float(equals[0][1]) == float(f):
                similar_fracs = equals

        if similar_fracs is not None:
            print(f"Похожие записи – {similar_fracs}")
            return

        similar_frac = fractions.find(f)
        if similar_frac is not None:
            print(f"Найдена похожая запись – \"{similar_frac}\": {fractions[similar_frac]}")
            return

        print("Отсутствуют похожие числа")

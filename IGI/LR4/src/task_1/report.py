from .input import Input
from .fraction import Fraction, FracCollection


class Report(Input):
    """Printing some results"""

    @classmethod
    def input_frac(cls):
        nominator = cls._input_with_checking(int, "Enter the numerator: ")
        denominator = cls._input_with_checking(int, "Enter the denominator: ")

        frac = Fraction(nominator, denominator)
        return frac

    @classmethod
    def make(cls, fractions: FracCollection, f: Fraction):
        print(f"\nChecking the number: {f}")
        cls.__relation_report(fractions, f)
        cls.__similars_report(fractions, f)

    @staticmethod
    def __relation_report(fractions: FracCollection, f: Fraction):
        max_fr = fractions.max()[1]
        if float(f) > float(max_fr):
            relation_string = "more"
        elif float(f) == float(max_fr):
            relation_string = "equal"
        else:
            relation_string = "less"
        print(f"Entered number is {relation_string} than max in the dictionary")

    @staticmethod
    def __similars_report(fractions: FracCollection, f: Fraction):
        equals_list = fractions.find_equals()

        similar_fracs = None
        for equals in equals_list:
            if float(equals[0][1]) == float(f):
                similar_fracs = equals

        if similar_fracs is not None:
            print(f"Similar records – {similar_fracs}")
            return

        similar_frac = fractions.find(f)
        if similar_frac is not None:
            print(f"Similar record found – \"{similar_frac}\": {fractions[similar_frac]}")
            return

        print("There is no similar records")

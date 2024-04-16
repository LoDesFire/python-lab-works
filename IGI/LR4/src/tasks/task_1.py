from src.task_1 import Report, Fraction, FracCollection, PickleSerializer
from src.task_1.csv_serializer import CSVSerializer

numbers = {
    "one": Fraction(10000, 10000),
    "one_2": Fraction(76, 76),
    "minus_one_fiftieth": Fraction(-1, 50),
    "half": Fraction(1, 2),
    "two_thirds": Fraction(2, 3),
    "three_fourths": Fraction(3, 4),
    "five": Fraction(20, 4),
    "one_twentieth": Fraction(1, 20),
    "and_minus_one_fiftieth": Fraction(40, -2000),
    "a_half": Fraction(45, 90)
}


def task_1():
    """Launching task 1"""
    pickleSerializer = PickleSerializer("src/task_1/data/binary.bin")
    csvSerializer = CSVSerializer("src/task_1/data/data.csv")

    pickleSerializer.save(FracCollection(numbers))
    csvSerializer.save(pickleSerializer.obtain())
    fractions = csvSerializer.obtain()

    frac = Report.input_frac()

    Report.make(fractions, frac)


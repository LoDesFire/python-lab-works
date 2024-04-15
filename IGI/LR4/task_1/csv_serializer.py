from task_1 import FracCollection, Fraction
import csv


class CSVSerializer:
    def __init__(self, path):
        self.__path = path

    headers = ["key", "numerator", "denominator"]

    def save(self, frac_collection: FracCollection):
        with open(self.__path, "w") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers, dialect="excel")
            writer.writeheader()

            for row in frac_collection.to_csv_list():
                writer.writerow(row)

    def obtain(self):
        dictionary = dict()
        with open(self.__path, "r") as file:
            reader = csv.DictReader(file, fieldnames=self.headers, dialect="excel")
            for row in reader:
                if row[self.headers[0]] != self.headers[0]:
                    dictionary.update({row[self.headers[0]]: Fraction(int(row[self.headers[1]]), int(row[self.headers[2]]))})

        return FracCollection(dictionary)



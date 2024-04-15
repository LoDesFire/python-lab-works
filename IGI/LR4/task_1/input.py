
class Input:
    @staticmethod
    def _input_with_checking(_type: type, phrase: str):
        while True:
            try:
                nominator = _type(input(phrase))
                return nominator
            except ValueError:
                print("Попробуй заново...\n")
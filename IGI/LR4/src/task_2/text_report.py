import re


class TextReport:
    """Processing the text according to the specific rules"""

    def __init__(self, text='') -> None:
        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, input_text):
        self.__text = input_text

    def sentences_count(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[!?.]', self.__text)
        return len(sentences)

    def decl_sent_count(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*\.', self.__text)
        return len(sentences)

    def excl_sent_count(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*!', self.__text)
        return len(sentences)

    def interrog_sent_count(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*\?', self.__text)
        return len(sentences)

    def avg_sent_size(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[!?.]', self.__text)
        sizesum = 0
        for snt in sentences:
            sizesum += len(re.split(r"[,; ]", snt))
        return sizesum / len(sentences)

    def avg_word_size(self):
        wordCounter = 0
        sizeSum = 0
        for w in self.words_list():
            wordCounter += 1
            sizeSum += len(w)
        return sizeSum / wordCounter

    def emojis_count(self):
        emojis = re.findall(r'([:;]-+(\[+|]+|\(+|\)+))', self.__text)
        return len(emojis)

    def all_capital_symbols(self):
        return re.findall(r'[A-Z]', self.__text)

    @staticmethod
    def replace_sequence(text):
        return re.sub(r'p.*?pb.*?bc.*?c', 'ddd', text)

    def words_list(self):
        words_list = re.split(r"[,;.!?\n ]", self.__text)
        return [w for w in words_list if w != ""]

    def words_less_five(self):
        return sum(1 for w in self.words_list() if len(w) < 5)

    def find_smallest_word_ends_d(self):
        word = ''
        minWordSize = 1e9
        for w in self.words_list():
            if w.endswith('d') and len(w) < minWordSize:
                word = w
                minWordSize = len(word)
        return word

    def sort_words(self):
        return sorted(self.words_list(), key=lambda x: len(x), reverse=True)

import re


class TextReport:

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
            snt = snt.replace(',', '').replace(';', '')
            sizesum += len(snt.split())
        return sizesum / len(sentences)

    def avg_word_size(self):
        text = self.__text.replace(',', '') \
            .replace(';', '').replace('.', '') \
            .replace('!', '').replace('?', '').replace('\n', '')
        wordCounter = 0
        sizeSum = 0
        for w in text.split():
            if w == '':
                continue
            wordCounter += 1
            sizeSum += len(w)
        return sizeSum / wordCounter

    def emojis_count(self):
        emojis = re.findall(r'([:;]-+(\[+|]+|\(+|\)+))', self.__text)
        return len(emojis)

    def all_capital_symbols(self):
        return re.findall(r'[A-Z]', self.__text)

    def replace_sequence(self):
        sequences = re.findall(r'p.*?pb.*?bc.*?c', self.__text)
        text: str = self.__text
        for sequence in sorted(sequences, key=lambda s: len(s)):
            text = text.replace(sequence, "ddd")

        return text

    def words_list(self):
        text = self.__text.replace(',', '') \
            .replace(';', '').replace('.', '') \
            .replace('!', '').replace('?', '').replace('\n', '')
        lst = []
        for w in text.split():
            if w == '':
                continue
            lst.append(w)
        return lst

    def words_less_five(self):
        text = self.__text.replace(',', '') \
            .replace(';', '').replace('.', '') \
            .replace('!', '').replace('?', '').replace('\n', '')
        return sum(1 for w in text.split() if len(w) < 5)

    def find_smallest_word_ends_d(self):
        text = self.__text.replace(',', '') \
            .replace(';', '').replace('.', '') \
            .replace('!', '').replace('?', '').replace('\n', '')

        aword = ''
        awordSize = 1e9
        for w in text.split():
            if w.endswith('d') and len(w) < awordSize:
                aword = w
                awordSize = len(aword)
        return aword

    def sort_words(self):
        return sorted(self.words_list(), key=lambda x: len(x), reverse=True)


TextReport("ppppbbccpbbccpbbccc").replace_sequence()

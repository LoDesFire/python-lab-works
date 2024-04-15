from task_2 import TextReport
import zipfile


def task2():
    top = TextReport()
    with open("task_2/data/text.txt", 'r') as f:
        text = f.read()
        top.text = text

    with open("task_2/data/report.txt", 'w') as f:
        print(f"Sentences count: {top.sentences_count()}\n")
        f.write(f"Sentences count: {top.sentences_count()}\n")

        print(f"Declaritive sentences count: {top.decl_sent_count()}\n")
        f.write(f"Declaritive sentences count: {top.decl_sent_count()}\n")

        print(f"Exclamation sentences count: {top.excl_sent_count()}\n")
        f.write(f"Exclamation sentences count: {top.excl_sent_count()}\n")

        print(f"Interrogative sentences count: {top.interrog_sent_count()}\n")
        f.write(f"Interrogative sentences count: {top.interrog_sent_count()}\n")

        print(f"Average size of sentences: {top.avg_sent_size()}\n")
        f.write(f"Average size of sentences: {top.avg_sent_size()}\n")

        print(f"Average size of words: {top.avg_word_size()}\n")
        f.write(f"Average size of words:  {top.avg_word_size()}\n")

        print(f"Emojis count: {top.emojis_count()}\n")
        f.write(f"Emojis count: {top.emojis_count()}\n")

        print(f"Words count: {len(top.words_list())}\n")
        f.write(f"Words count: {len(top.words_list())}\n")

        print(f"Word list: {top.words_list()}\n")
        f.write(f"Word list: {top.words_list()}\n")

        print(f"Capital letters: {top.all_capital_symbols()}\n")
        f.write(f"Capital letters: {top.all_capital_symbols()}\n")

        print(f"Count of words with size less than 5: {top.words_less_five()}\n")
        f.write(f"Count of words with size less than 5: {top.words_list()}\n")

        print(f"Smallest word ends with 'd': {top.find_smallest_word_ends_d()}\n")
        f.write(f"Smallest word ends with 'd': {top.find_smallest_word_ends_d()}\n")

        print(f"Sorted list of words: {top.sort_words()}\n")
        f.write(f"Sorted list of words: {top.sort_words()}\n")

    with zipfile.ZipFile("task_2/data/myzip.zip", 'w') as myzip:
        myzip.write("task_2/data/report.txt")


if __name__ == "__main__":
    task2()

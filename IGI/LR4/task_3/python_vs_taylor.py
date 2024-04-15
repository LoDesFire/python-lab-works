import matplotlib.pyplot as plt
import math
import statistics

class PythonVsTaylor:

    @staticmethod
    def __save_plot(x, y_t, y_m, path='task_3/graph.png'):
        """Function for plot."""
        plt.plot(x, y_t, label='taylor asin')
        plt.plot(x, y_m, label='python asin')

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()

        plt.grid(visible=True)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')

        plt.savefig(path)

    @staticmethod
    def __asin_taylor(x, eps=0.1):
        sm = 0
        iter_count = 0
        arcsin_math = math.asin(x)

        while abs(sm - arcsin_math) > eps and iter_count < 500:
            sm += math.factorial(2 * iter_count) / (
                    4 ** iter_count * math.factorial(iter_count) ** 2 * (2 * iter_count + 1)) * x ** (2 * iter_count + 1)
            iter_count += 1

        return sm

    @classmethod
    def run(cls, taylor_eps=0.1):
        y_t = []
        y_m = []
        xs = []
        for x in map(lambda i: i / 100, range(-100, 100, 1)):
            xs.append(x)
            y_t.append(cls.__asin_taylor(x, taylor_eps))
            y_m.append(math.asin(x))

        print(f"Среднее арифметическое = {statistics.mean(y_t)}")
        print(f"Медиана = {statistics.median(y_t)}")
        print(f"Мода = {statistics.mode(y_t)}")
        print(f"Дисперсия = {statistics.variance(y_t)}")
        print(f"Среднеквадратичное отклонение = {statistics.stdev(y_t)}")

        cls.__save_plot(xs, y_t, y_m)


import numpy as np
import collections
from tkinter import ttk
from numba import njit


#Принимает два масива векторов, возвращает евклидово расстояние.
@njit
def evclid_dist(vector1, vector2):
    return np.sqrt(np.sum((vector1 - vector2)**2))

class Calculate:
    __min_distans = np.zeros((1, 3), dtype=float)  # Индексы 0 и 1 - пары векторов, 2 - их расстояние.
    __max_distans = np.zeros((1, 3), dtype=float)
    __dist_bins = []  # Список бункеров для гистограммы.
    __dist_values = []  # Список значений для гистограммы.

    def get_min_distans(self):
        return self.__min_distans

    def get_max_distans(self):
        return self.__max_distans

    def get_dist_values(self):
        return self.__dist_values

    def get_dist_bins(self):
        return self.__dist_bins

    # Считает минимальное и максимальное расстояние, формирует данные для гистограммы
    def calc_dist(self, vector, res_window):
        self.__min_distans = [0, 0, 100]
        self.__max_distans = [0, 0, 0]
        dist_dict = {}  # Ключ - округленное расстояние, значение - частота.
        size_vector = len(vector)

        # Создает виджет процесса расчетов.
        progress_bar = ttk.Progressbar(res_window, orient='horizontal', length=400, mode='determinate', maximum=100)
        progress_bar.pack()
        progress_bar['maximum'] = 100

        # Перебирает уникальные пары векторов, считает их расстояние.
        for i in range(size_vector):
            # Рисует прогресс пока высчитываются расстояния.
            if i % 100 == 0:
                progress_bar['value'] = i / size_vector * 100
                progress_bar.update()

            for j in range(i + 1, size_vector):
                dist = evclid_dist(vector[i], vector[j])

                # Формирует словарь с данными для гистограммы.
                if dist_dict.get(round(dist, 1)) == None:
                    dist_dict[round(dist, 1)] = 1
                else:
                    dist_dict[round(dist, 1)] += 1

                # Получаем пары вектором и их минимальное и максимальное расстояние.
                if dist > self.__max_distans[2]:
                    self.__max_distans[0] = i
                    self.__max_distans[1] = j
                    self.__max_distans[2] = dist
                elif dist < self.__min_distans[2]:
                    self.__min_distans[0] = i
                    self.__min_distans[1] = j
                    self.__min_distans[2] = dist

        # Сортируем словарь для построения гистограммы.
        sorted_dist_dict = collections.OrderedDict(sorted(dist_dict.items()))
        self.__dist_bins = list(sorted_dist_dict.keys())
        self.__dist_values = list(sorted_dist_dict.values())

        # Удаляем виджет прогресса после расчетов.
        progress_bar.destroy()
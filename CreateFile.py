import random
import csv
import numpy as np
from tkinter import filedialog as fd


class CreateFile:
    # Формируем список векторов.
    def __init__(self, n, m):
        vector = np.zeros([n, m])
        for i in range(len(vector)):
            for j in range(len(vector[i])):
                vector[i, j] = random.uniform(-1, 1)
        self.save_vector(vector)

    # Запись списка векторов в файл csv.
    def save_vector(self, vector):
        formats = [('Comma Separated values', '*.csv'), ]
        file_name = fd.asksaveasfilename(title="Сохранить файл", filetypes=formats, initialfile="vector.csv")
        with open(file_name, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in vector:
                writer.writerow(line)

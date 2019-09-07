from numpy import genfromtxt
from tkinter import filedialog as fd


class LoadFile:
    # Считываем вектора из файла в список
    def read_file(self):
        formats = [('Comma Separated values', '*.csv'), ]
        file_name = fd.askopenfilename(title="Загрузить csv-файл", filetypes=formats)

        vector_list = genfromtxt(file_name, delimiter=',')

        return vector_list

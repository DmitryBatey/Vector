from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import Calculate as Calc
import numpy as np
import matplotlib

matplotlib.use('TkAgg')


class ResultWindow(tk.Toplevel):
    def __init__(self, vector_list):
        super().__init__()
        self.init_result_window(vector_list)

    def init_result_window(self, vector_list):
        self.title("Расчеты")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.geometry('600x550+{}+{}'.format(400, 100))

        wait_lab = tk.Label(self, text="Идет расчёт результатов, это может занять немного времени")
        wait_lab.pack()
        self.update()

        calc_obj = Calc.Calculate()
        calc_obj.calc_dist(vector_list, self)
        min_dist = calc_obj.get_min_distans()
        max_dist = calc_obj.get_max_distans()

        wait_lab.destroy()

        min_labl = tk.Label(self, text=("Минимальное расстояние: " + str(min_dist[2])))
        max_labl = tk.Label(self, text=("Максимальное расстояние: " + str(max_dist[2])))

        frame1 = tk.Frame(self)
        frame2 = tk.Frame(self)

        lbox_min = tk.Listbox(frame1, width=100, height=2)
        lbox_max = tk.Listbox(frame2, width=100, height=2)

        for i in range(2):
            lbox_min.insert(i, ("Вектор №" + str(min_dist[i] + 1) + " " + str(vector_list[min_dist[i]])))
            lbox_max.insert(i, ("Вектор №" + str(max_dist[i] + 1) + " " + str(vector_list[max_dist[i]])))

        scroll_min = tk.Scrollbar(frame1, orient='horizontal', command=lbox_min.xview)
        scroll_max = tk.Scrollbar(frame2, orient='horizontal', command=lbox_max.xview)
        lbox_min.config(xscrollcommand=scroll_min.set)
        lbox_max.config(xscrollcommand=scroll_max.set)

        # Отображает пары векторов с минимальным и максимальным расстояниям.
        frame1.pack()
        lbox_min.pack()
        scroll_min.pack(side='bottom', fill='x')
        min_labl.pack()

        frame2.pack()
        lbox_max.pack()
        scroll_max.pack(side='bottom', fill='x')
        max_labl.pack()

        # Рисует гистограмму.
        fig = Figure(figsize=(6, 6))
        ax = fig.add_subplot(111)

        ax.set_title("Гистограмма распределения расстояний векторов")
        ax.grid(zorder=0)
        ax.bar(calc_obj.get_dist_bins(), calc_obj.get_dist_values(), 0.10, edgecolor='black', zorder=3)
        ax.set_xticks(np.arange(round(min_dist[2], 1), round(max_dist[2], 1), step=0.3))
        ax.set_xlabel('Расстояние')
        ax.set_ylabel('Частота')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()
        canvas.draw()

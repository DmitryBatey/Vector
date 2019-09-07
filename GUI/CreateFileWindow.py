import tkinter as tk
import CreateFile as cf


class CreateFile(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_create_file()

    def init_create_file(self):
        self.geometry("310x175+{}+{}".format(510, 200))
        self.title("Создание файла")
        self.resizable(False, False)
        self.update()
        self.grab_set()
        self.focus_set()

        vcmd = (self.register(self.callback))

        label_N = tk.Label(self, text="Введите количество векторов N:\n(500 < N ≤ 1000)")
        label_M = tk.Label(self, text="Введите размерность векторов M:\n(10 < M ≤ 50)")
        self.error1 = tk.Label(self, fg='red')

        self.entry_N = tk.Entry(self, width=6, validate='all', validatecommand=(vcmd, '%P'))
        self.entry_M = tk.Entry(self, width=6, validate='all', validatecommand=(vcmd, '%P'))

        btn_ok = tk.Button(self, width=10, height=2, text="OK",
                           command=self.num_test)
        btn_cancel = tk.Button(self, width=10, height=2, text="Отмена",
                               command=lambda: self.destroy())

        label_N.place(x=0, y=10)
        label_M.place(x=0, y=60)
        self.entry_N.place(x=235, y=10)
        self.entry_M.place(x=235, y=60)
        btn_ok.place(x=18, y=130)
        btn_cancel.place(x=200, y=130)

    # Ограничивает ввод символов кроме чисел.
    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    # Проверяет введенные числа на соответствие условиям.
    def num_test(self):
        try:
            n = int(self.entry_N.get())
            m = int(self.entry_M.get())
            self.error1.config(text="")

            if all([(n > 500), (n <= 1000), (m > 10), (m <= 50)]):
                cf.CreateFile(n, m)
                self.destroy()
            else:
                raise Exception("Введенные неверные значения")
        except ValueError:
            self.error1.config(text="Введены не все значения")
            self.error1.place(x=60, y=100)
        except OSError:
            pass
        except Exception as e:
            self.error1.config(text=e)
            self.error1.place(x=50, y=100)

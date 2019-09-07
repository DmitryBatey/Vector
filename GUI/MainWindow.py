import tkinter as tk
import LoadFile as ld
from GUI import CreateFileWindow as cfw, ResultWindow as rw


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        btn_create_file = tk.Button(width=40, height=3, text="Создать файл с векторами",
                                    command=lambda: cfw.CreateFile())
        btn_load_file = tk.Button(width=40, height=3, text="Загрузить файл для расчетов",
                                  command=lambda: self.load_file())
        self.error_lab = tk.Label(fg='red')

        btn_create_file.place(x=8, y=10)
        btn_load_file.place(x=8, y=80)
        self.error_lab.place(x=130, y=150)

    # Загрузка файла
    def load_file(self):
        try:
            vector_list = ld.LoadFile().read_file()
        except Exception:
            self.error_lab.config(text="Файл не загружен")

        rw.ResultWindow(vector_list)


def main():
    root = tk.Tk()
    app = MainWindow(root)
    app.pack()
    root.title("Расчет расстояний векторов")
    root.width, root.height = root.winfo_screenwidth() // 2 - 150, \
                              root.winfo_screenheight() // 2 - 268
    root.geometry('380x200+{}+{}'.format(root.width, root.height))
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()

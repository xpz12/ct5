import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Что мне делать, как мне жить?")
        self.root.configure(bg="black")
        self.root.geometry("700x450")

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Мои текущие задачи",
            fg="yellow",
            bg="black",
            font=("Arial", 22, "underline")
        )
        title.pack(pady=(15, 10))

        frame = tk.Frame(self.root, bg="black")
        frame.pack(expand=True)

        tasks = [
            ("Прошло 741 дней от Крутая лаба", "red"),
            ("Прошло 740 дней от Что-то произойдет", "red"),
            ("Прошло 479 дней от Окончания карантина", "red"),
            ("Прошло 150 дней от Начало следующего семестра", "red"),
            ("Прямо щаз происходит Скоро экзамен", "orange"),
            ("Осталось 139 дней до Навестить бабушку", "gray"),
            ("Осталось 170 дней до Сходить в кино", "gray"),
            ("Осталось 200 дней до Новый 2024 год", "gray"),
            ("Остался 211 дней до Пришельцы атакуют Землю", "gray"),
            ("Осталось 328 дней до Надо сдать лабу", "gray"),
        ]

        for text, color in tasks:
            label = tk.Label(
                frame,
                text=text,
                fg=color,
                bg="black",
                font=("Arial", 14),
                anchor="w",
                justify="left"
            )

            label.pack(
                fill="x",
                pady=1,
                padx=20
            )


root = tk.Tk()
app = TodoApp(root)
root.mainloop()

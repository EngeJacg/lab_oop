import tkinter as tk
from tkinter import messagebox


class SafeCalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Безопасный калькулятор")
        self.window.geometry("330x300")
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="Проверка деления и формата",
                 font=("Arial", 13, "bold")).pack(pady=12)

        panel = tk.Frame(self.window)
        panel.pack(pady=12)

        tk.Label(panel, text="Число 1:").grid(row=0, column=0, padx=6)
        self.val1_input = tk.Entry(panel, width=12)
        self.val1_input.grid(row=0, column=1, padx=6)
        self.val1_input.insert(0, "12")

        tk.Label(panel, text="Число 2:").grid(row=1, column=0, padx=6, pady=10)
        self.val2_input = tk.Entry(panel, width=12)
        self.val2_input.grid(row=1, column=1, padx=6, pady=10)
        self.val2_input.insert(0, "4")

        tk.Label(self.window, text="Выберите действие:").pack()

        self.operation = tk.StringVar(value="+")
        operations = [("Сложение", "+"), ("Вычитание", "-"),
                      ("Умножение", "*"), ("Деление", "/")]
        op_frame = tk.Frame(self.window)
        op_frame.pack(pady=10)

        for i, (text, value) in enumerate(operations):
            tk.Radiobutton(op_frame, text=text, variable=self.operation,
                           value=value).grid(row=0, column=i, padx=5)

        tk.Button(self.window, text="Вычислить", command=self.perform_calculation,
                  bg="#d4edda", font=("Arial", 10), width=14).pack(pady=14)

        result_frame = tk.Frame(self.window)
        result_frame.pack(pady=10)

        tk.Label(result_frame, text="Итог:",
                 font=("Arial", 11, "bold")).pack(side="left")

        self.output = tk.Label(result_frame, text="—",
                               font=("Arial", 11), fg="#155724",
                               width=12, relief="solid", padx=8, pady=4)
        self.output.pack(side="left", padx=10)

        tk.Button(self.window, text="Сброс", command=self.reset_inputs,
                  width=14).pack(pady=6)

    def perform_calculation(self):
        val1_text = self.val1_input.get().strip()
        val2_text = self.val2_input.get().strip()
        op = self.operation.get()

        if not val1_text or not val2_text:
            messagebox.showerror("Ошибка", "Оба поля должны содержать значения")
            self.output.config(text="Ошибка!", fg="#721c24")
            return

        try:
            num1 = float(val1_text)
        except ValueError:
            messagebox.showerror("Ошибка формата", "Первое число имеет неверный формат")
            self.val1_input.config(bg="#f8d7da")
            self.output.config(text="Ошибка!", fg="#721c24")
            return

        try:
            num2 = float(val2_text)
        except ValueError:
            messagebox.showerror("Ошибка формата", "Второе число имеет неверный формат")
            self.val2_input.config(bg="#f8d7da")
            self.output.config(text="Ошибка!", fg="#721c24")
            return

        self.val1_input.config(bg="white")
        self.val2_input.config(bg="white")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Деление на ноль", "Деление на ноль недопустимо")
                self.val2_input.config(bg="#f8d7da")
                self.output.config(text="Ошибка!", fg="#721c24")
                return
            result = num1 / num2

        self.output.config(text=f"{result:.4f}", fg="#155724")

    def reset_inputs(self):
        self.val1_input.delete(0, tk.END)
        self.val1_input.insert(0, "12")
        self.val2_input.delete(0, tk.END)
        self.val2_input.insert(0, "4")
        self.operation.set("+")
        self.output.config(text="—", fg="#155724")
        self.val1_input.config(bg="white")
        self.val2_input.config(bg="white")


if __name__ == "__main__":
    main_window = tk.Tk()
    app = SafeCalculator(main_window)
    main_window.mainloop()
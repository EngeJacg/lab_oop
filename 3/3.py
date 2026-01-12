import tkinter as tk
from abc import ABC, abstractmethod
import math

class IntegerOperation(ABC):
    @abstractmethod
    def get_operation_name(self):
        pass

    @abstractmethod
    def get_symbol(self):
        pass

    @abstractmethod
    def perform_calculation(self, x, y):
        pass

class IntegerDivision(IntegerOperation):
    def get_operation_name(self):
        return "Целочисленное деление"

    def get_symbol(self):
        return "DIV"

    def perform_calculation(self, x, y):
        return x // y if y != 0 else "Ошибка"

class RemainderOperation(IntegerOperation):
    def get_operation_name(self):
        return "Остаток от деления"

    def get_symbol(self):
        return "MOD"

    def perform_calculation(self, x, y):
        return x % y if y != 0 else "Ошибка"

class GreatestCommonDivisor(IntegerOperation):
    def get_operation_name(self):
        return "Наибольший общий делитель"

    def get_symbol(self):
        return "НОД"

    def perform_calculation(self, x, y):
        return math.gcd(x, y) if x != 0 or y != 0 else "Ошибка"

class LeastCommonMultiple(IntegerOperation):
    def get_operation_name(self):
        return "Наименьшее общее кратное"

    def get_symbol(self):
        return "НОК"

    def perform_calculation(self, x, y):
        if x == 0 or y == 0:
            return 0
        return abs(x * y) // math.gcd(x, y)

class BinaryOperationsApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Целочисленные бинарные операции")
        self.window.geometry("350x350")

        self.operations = [
            IntegerDivision(),
            RemainderOperation(),
            GreatestCommonDivisor(),
            LeastCommonMultiple()
        ]

        tk.Label(window, text="Целочисленные операции", font=("Arial", 14, "bold")).pack(pady=15)

        self.selected_operation = tk.StringVar(value="Целочисленное деление")
        for op in self.operations:
            tk.Radiobutton(window, text=op.get_operation_name(),
                         variable=self.selected_operation,
                         value=op.get_operation_name()).pack(anchor="w", padx=20)

        input_frame = tk.Frame(window)
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Число A:").grid(row=0, column=0, padx=5, pady=5)
        self.input_a = tk.Entry(input_frame, width=10)
        self.input_a.grid(row=0, column=1, padx=5, pady=5)
        self.input_a.insert(0, "15")

        tk.Label(input_frame, text="Число B:").grid(row=1, column=0, padx=5, pady=5)
        self.input_b = tk.Entry(input_frame, width=10)
        self.input_b.grid(row=1, column=1, padx=5, pady=5)
        self.input_b.insert(0, "4")

        tk.Button(window, text="Выполнить операцию",
                command=self.execute_operation,
                width=20).pack(pady=15)

        self.result_label = tk.Label(window, text="Результат: ",
                                   font=("Arial", 12), fg="blue")
        self.result_label.pack()

    def execute_operation(self):
        try:
            a = int(self.input_a.get())
            b = int(self.input_b.get())

            for operation in self.operations:
                if operation.get_operation_name() == self.selected_operation.get():
                    result = operation.perform_calculation(a, b)
                    symbol = operation.get_symbol()
                    self.result_label.config(
                        text=f"Результат: {a} {symbol} {b} = {result}"
                    )
                    break
        except ValueError:
            self.result_label.config(text="Ошибка: введите целые числа!", fg="red")
        except ZeroDivisionError:
            self.result_label.config(text="Ошибка: деление на ноль!", fg="red")

if __name__ == "__main__":
    window = tk.Tk()
    app = BinaryOperationsApp(window)
    window.mainloop()
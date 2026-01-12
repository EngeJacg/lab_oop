import tkinter as tk
from tkinter import messagebox


class PizzaOrderApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Заказ пиццы")
        self.window.geometry("350x500")

        self.pizza_prices = {
            "Маргарита": 450,
            "Пепперони": 550,
            "Гавайская": 500,
            "Четыре сыра": 600
        }

        self.create_interface()

    def create_interface(self):

        tk.Label(self.window, text="Пиццерия",
                 font=("Arial", 16, "bold"), fg="red").pack(pady=15)

        tk.Label(self.window, text="Выберите пиццу:",
                 font=("Arial", 10)).pack()
        self.selected_pizza = tk.StringVar(value="Маргарита")

        pizza_frame = tk.Frame(self.window)
        pizza_frame.pack(pady=8)

        for pizza_name in self.pizza_prices:
            rb = tk.Radiobutton(
                pizza_frame,
                text=f"{pizza_name} - {self.pizza_prices[pizza_name]} руб.",
                variable=self.selected_pizza,
                value=pizza_name,
                font=("Arial", 9)
            )
            rb.pack(anchor="w", pady=2)

        tk.Label(self.window, text="Количество:",
                 font=("Arial", 10)).pack(pady=(15, 5))
        self.quantity_var = tk.IntVar(value=1)
        tk.Spinbox(
            self.window,
            from_=1,
            to=5,
            textvariable=self.quantity_var,
            width=8,
            font=("Arial", 10)
        ).pack()

        tk.Label(self.window, text="Дополнительно:",
                 font=("Arial", 10)).pack(pady=(20, 10))

        self.extra_cheese = tk.BooleanVar()
        tk.Checkbutton(
            self.window,
            text="Дополнительный сыр (+80 руб.)",
            variable=self.extra_cheese,
            font=("Arial", 9)
        ).pack(pady=2)

        self.extra_pepperoni = tk.BooleanVar()
        tk.Checkbutton(
            self.window,
            text="Дополнительный пепперони (+100 руб.)",
            variable=self.extra_pepperoni,
            font=("Arial", 9)
        ).pack(pady=2)

        self.garlic_sauce = tk.BooleanVar()
        tk.Checkbutton(
            self.window,
            text="Чесночный соус (+50 руб.)",
            variable=self.garlic_sauce,
            font=("Arial", 9)
        ).pack(pady=2)

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=25)

        tk.Button(
            button_frame,
            text="Рассчитать",
            command=self.calculate_order,
            bg="lightgreen",
            width=12,
            font=("Arial", 10, "bold")
        ).pack(side="left", padx=8)

        tk.Button(
            button_frame,
            text="Новый заказ",
            command=self.reset_order,
            bg="lightcoral",
            width=12,
            font=("Arial", 10, "bold")
        ).pack(side="left", padx=8)

        self.result_text = tk.StringVar(value="Сумма заказа: 0 руб.")
        self.result_label = tk.Label(
            self.window,
            textvariable=self.result_text,
            font=("Arial", 12, "bold"),
            fg="darkblue",
            bg="lightyellow",
            relief="ridge",
            padx=20,
            pady=5
        )
        self.result_label.pack(pady=15)

    def calculate_order(self):
        try:
            pizza_type = self.selected_pizza.get()
            base_price = self.pizza_prices[pizza_type]

            extras_total = 0
            if self.extra_cheese.get():
                extras_total += 80
            if self.extra_pepperoni.get():
                extras_total += 100
            if self.garlic_sauce.get():
                extras_total += 50

            quantity = self.quantity_var.get()
            price_for_one = base_price + extras_total
            total_price = price_for_one * quantity

            self.result_text.set(f"Сумма заказа: {total_price} руб.")

            order_details = f"""
            ДЕТАЛИ ЗАКАЗА:

            Пицца: {pizza_type}
            Цена за одну: {base_price} руб.

            Дополнительно:"""

            if extras_total > 0:
                if self.extra_cheese.get():
                    order_details += "\n   • Доп. сыр: 80 руб."
                if self.extra_pepperoni.get():
                    order_details += "\n   • Доп. пепперони: 100 руб."
                if self.garlic_sauce.get():
                    order_details += "\n   • Чесночный соус: 50 руб."
            else:
                order_details += "\n   Без дополнительных ингредиентов"

            order_details += f"\n\nКоличество: {quantity}"
            order_details += f"\nИтого к оплате: {total_price} руб."
            order_details += f"\n\nСпасибо за заказ!"

            messagebox.showinfo("Ваш заказ", order_details)

        except Exception:
            messagebox.showerror("Ошибка", "Пожалуйста, проверьте введенные данные")

    def reset_order(self):
        self.selected_pizza.set("Маргарита")
        self.quantity_var.set(1)
        self.extra_cheese.set(False)
        self.extra_pepperoni.set(False)
        self.garlic_sauce.set(False)
        self.result_text.set("Сумма заказа: 0 руб.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderApp(root)
    root.mainloop()
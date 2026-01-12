import tkinter as tk
from tkinter import ttk


class EventsApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Приложение событий")
        self.master.geometry("680x480")

        self.tabs_container = ttk.Notebook(master)
        self.tabs_container.pack(fill="both", expand=True, padx=8, pady=8)

        self.page_one = ttk.Frame(self.tabs_container)
        self.page_two = ttk.Frame(self.tabs_container)
        self.page_three = ttk.Frame(self.tabs_container)

        self.tabs_container.add(self.page_one, text="Страны мира")
        self.tabs_container.add(self.page_two, text="Настройки профиля")
        self.tabs_container.add(self.page_three, text="Преобразование чисел")

        self.setup_first_page()
        self.setup_second_page()
        self.setup_third_page()

    def setup_first_page(self):
        self.country_info = {
            "Канада": {"столица": "Оттава", "площадь": "9.98 млн км²", "валюта": "канадский доллар",
                       "часовой пояс": "UTC-3:30 до UTC-8"},
            "Австралия": {"столица": "Канберра", "площадь": "7.69 млн км²", "валюта": "австралийский доллар",
                          "часовой пояс": "UTC+8 до UTC+10:30"},
            "Италия": {"столица": "Рим", "площадь": "301 тыс. км²", "валюта": "евро", "часовой пояс": "UTC+1"},
            "Южная Корея": {"столица": "Сеул", "площадь": "100 тыс. км²", "валюта": "южнокорейская вона",
                            "часовой пояс": "UTC+9"},
            "Мексика": {"столица": "Мехико", "площадь": "1.96 млн км²", "валюта": "мексиканское песо",
                        "часовой пояс": "UTC-5 до UTC-8"}
        }

        tk.Label(self.page_one, text="Мировые страны",
                 font=("Arial", 13, "bold")).pack(pady=12)

        container = tk.Frame(self.page_one)
        container.pack(pady=12)

        tk.Label(container, text="Выберите страну:").pack(side="left")

        self.selected_country = tk.StringVar()
        self.country_selector = ttk.Combobox(
            container,
            textvariable=self.selected_country,
            values=list(self.country_info.keys()),
            width=18,
            state="readonly"
        )
        self.country_selector.pack(side="left", padx=8)
        self.country_selector.bind("<<ComboboxSelected>>", self.country_changed)

        self.info_display = tk.Text(self.page_one, height=9, width=55,
                                    font=("Arial", 10))
        self.info_display.pack(pady=12, padx=18)
        self.info_display.insert("1.0", "Информация о странах появится после выбора")
        self.info_display.config(state="disabled")

    def country_changed(self, event):
        country = self.selected_country.get()
        if country in self.country_info:
            data = self.country_info[country]
            self.info_display.config(state="normal")
            self.info_display.delete("1.0", tk.END)

            content = f" {country}:\n\n"
            content += f"• Столица: {data['столица']}\n"
            content += f"• Площадь: {data['площадь']}\n"
            content += f"• Валюта: {data['валюта']}\n"
            content += f"• Часовой пояс: {data['часовой пояс']}\n"

            self.info_display.insert("1.0", content)
            self.info_display.config(state="disabled")

    def setup_second_page(self):
        tk.Label(self.page_two, text="Персональные настройки",
                 font=("Arial", 13, "bold")).pack(pady=12)

        self.options_state = {}
        options_list = [
            ("Автосохранение", "Автоматически сохранять изменения"),
            ("Темная тема", "Использовать темный режим"),
            ("Двухфакторная аутентификация", "Защитить аккаунт 2FA"),
            ("Офлайн-доступ", "Работать без интернета"),
            ("Уведомления о безопасности", "Предупреждения о подозрительной активности"),
            ("Экспорт истории", "Сохранять историю действий"),
            ("Синхронизация между устройствами", "Общие данные на всех устройствах")
        ]

        for idx, (key, text) in enumerate(options_list):
            state_var = tk.BooleanVar(value=True if idx < 3 else False)
            self.options_state[key] = state_var

            check_button = tk.Checkbutton(
                self.page_two,
                text=text,
                variable=state_var,
                command=lambda k=key: self.option_updated(k)
            )
            check_button.pack(anchor="w", padx=28, pady=3)

        self.status_text = tk.Label(self.page_two, text="Активных настроек: 3",
                                    font=("Arial", 10, "bold"), fg="darkblue")
        self.status_text.pack(pady=12)

        self.active_options = tk.Listbox(self.page_two, height=5, width=45)
        self.active_options.pack(pady=12)
        self.active_options.insert(0, "Автосохранение")
        self.active_options.insert(1, "Темная тема")
        self.active_options.insert(2, "Двухфакторная аутентификация")

    def option_updated(self, key):
        enabled = [k for k, v in self.options_state.items() if v.get()]
        total = len(enabled)

        self.status_text.config(text=f"Активных настроек: {total}")

        self.active_options.delete(0, tk.END)
        for item in enabled:
            self.active_options.insert(tk.END, item)

    def setup_third_page(self):
        tk.Label(self.page_three, text="Конвертер систем счисления",
                 font=("Arial", 13, "bold")).pack(pady=12)

        frame = tk.Frame(self.page_three)
        frame.pack(pady=12)

        tk.Label(frame, text="Целое число:").pack(side="left")

        self.input_value = tk.StringVar()
        self.input_field = tk.Entry(frame, textvariable=self.input_value,
                                    width=16, font=("Arial", 11))
        self.input_field.pack(side="left", padx=8)
        self.input_field.bind("<KeyRelease>", self.input_modified)

        results_container = tk.Frame(self.page_three)
        results_container.pack(pady=12, padx=18)

        systems = [
            ("Двоичная (bin):", "bin_result"),
            ("Восьмеричная (oct):", "oct_result"),
            ("Десятичная:", "dec_result"),
            ("Шестнадцатеричная (hex):", "hex_result")
        ]

        self.result_labels = {}

        for i, (label_text, var_name) in enumerate(systems):
            tk.Label(results_container, text=label_text,
                     font=("Arial", 10)).grid(row=i, column=0, sticky="w", pady=6)

            label = tk.Label(results_container, text="—",
                             font=("Courier", 10), bg="white", relief="sunken",
                             width=20, anchor="w")
            label.grid(row=i, column=1, sticky="w", padx=8, pady=6)
            self.result_labels[var_name] = label

    def input_modified(self, event):
        try:
            text = self.input_value.get()
            if text:
                value = int(text)

                self.result_labels['bin_result'].config(text=bin(value)[2:])
                self.result_labels['oct_result'].config(text=oct(value)[2:])
                self.result_labels['dec_result'].config(text=str(value))
                self.result_labels['hex_result'].config(text=hex(value)[2:].upper())
            else:
                self.reset_results()
        except ValueError:
            self.reset_results()

    def reset_results(self):
        for label in self.result_labels.values():
            label.config(text="—")


if __name__ == "__main__":
    window = tk.Tk()
    application = EventsApplication(window)
    window.mainloop()
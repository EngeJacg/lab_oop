import tkinter as tk
from tkinter import Listbox, END, MULTIPLE, messagebox


class ProjectTeamSelector:
    def __init__(self, window):
        self.window = window
        self.window.title("Формирование команды проекта")
        self.window.geometry("650x500")

        self.team_members = [
            "Аналитик", "Дизайнер", "Фронтенд", "Бэкенд",
            "Тестировщик", "Менеджер", "Архитектор", "DevOps",
            "Техлид", "Техписатель", "Маркетолог", "Аналитик данных"
        ]

        self.setup_gui()
        self.load_available_members()

    def setup_gui(self):
        self.create_title_bar()
        self.create_selection_area()
        self.bind_interactions()

    def create_title_bar(self):
        title_frame = tk.Frame(self.window, relief=tk.RIDGE, bd=2)
        title_frame.pack(side=tk.TOP, fill=tk.X, padx=8, pady=8)

        self.counter_display = tk.Label(
            title_frame,
            text="Всего ролей: 12 | В команде: 0",
            font=("Arial", 11, "bold")
        )
        self.counter_display.pack(side=tk.LEFT, padx=15)

        self.restart_button = tk.Button(
            title_frame,
            text="Начать заново",
            command=self.restart_team,
            bg="#e3f2fd",
            font=("Arial", 11)
        )
        self.restart_button.pack(side=tk.RIGHT, padx=8, pady=8)

    def create_selection_area(self):
        main_container = tk.Frame(self.window)
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        left_container = tk.LabelFrame(main_container, text="Доступные роли", padx=15, pady=15)
        left_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=8)

        self.roles_list = Listbox(
            left_container,
            selectmode=MULTIPLE,
            font=("Arial", 12),
            height=18,
            bg="#f5f5f5"
        )

        left_scroll = tk.Scrollbar(left_container, orient=tk.VERTICAL)
        left_scroll.config(command=self.roles_list.yview)
        self.roles_list.config(yscrollcommand=left_scroll.set)
        self.roles_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        left_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        button_container = tk.Frame(main_container)
        button_container.pack(side=tk.LEFT, fill=tk.Y, padx=15)

        self.add_role_button = tk.Button(
            button_container,
            text="Добавить ",
            command=self.add_to_team,
            font=("Arial", 12),
            width=12,
            height=2
        )
        self.add_role_button.pack(pady=15)

        self.add_all_button = tk.Button(
            button_container,
            text="Добавить всех ",
            command=self.add_all_to_team,
            font=("Arial", 12),
            width=12,
            height=2
        )
        self.add_all_button.pack(pady=15)

        self.remove_role_button = tk.Button(
            button_container,
            text="Убрать ",
            command=self.remove_from_team,
            font=("Arial", 12),
            width=12,
            height=2
        )
        self.remove_role_button.pack(pady=15)

        self.remove_all_button = tk.Button(
            button_container,
            text="Убрать всех ",
            command=self.remove_all_from_team,
            font=("Arial", 12),
            width=12,
            height=2
        )
        self.remove_all_button.pack(pady=15)

        right_container = tk.LabelFrame(main_container, text="Команда проекта", padx=15, pady=15)
        right_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=8)

        self.team_list = Listbox(
            right_container,
            selectmode=MULTIPLE,
            font=("Arial", 12),
            height=18,
            bg="#e8f5e9"
        )

        right_scroll = tk.Scrollbar(right_container, orient=tk.VERTICAL)
        right_scroll.config(command=self.team_list.yview)
        self.team_list.config(yscrollcommand=right_scroll.set)
        self.team_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        right_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def bind_interactions(self):
        self.roles_list.bind("<Double-Button-1>", lambda e: self.add_to_team())
        self.team_list.bind("<Double-Button-1>", lambda e: self.remove_from_team())
        self.roles_list.bind("<<ListboxSelect>>", self.update_display)
        self.team_list.bind("<<ListboxSelect>>", self.update_display)

    def load_available_members(self):
        self.roles_list.delete(0, END)
        for role in sorted(self.team_members):
            self.roles_list.insert(END, role)

    def add_to_team(self):
        selected_items = self.roles_list.curselection()

        if not selected_items:
            messagebox.showwarning("Внимание", "Выберите роли для добавления в команду!")
            return

        chosen_roles = [self.roles_list.get(i) for i in selected_items]

        for role in chosen_roles:
            self.team_list.insert(END, role)

        for i in reversed(selected_items):
            self.roles_list.delete(i)

        self.update_display()

    def add_all_to_team(self):
        if self.roles_list.size() == 0:
            messagebox.showinfo("Информация", "Нет доступных ролей")
            return

        all_roles = self.roles_list.get(0, END)
        for role in all_roles:
            self.team_list.insert(END, role)

        self.roles_list.delete(0, END)

        self.update_display()

    def remove_from_team(self):
        selected_items = self.team_list.curselection()

        if not selected_items:
            messagebox.showwarning("Внимание", "Выберите роли для удаления из команды!")
            return

        chosen_roles = [self.team_list.get(i) for i in selected_items]

        for role in chosen_roles:
            self.roles_list.insert(END, role)

        items = list(self.roles_list.get(0, END))
        items.sort()
        self.roles_list.delete(0, END)
        for item in items:
            self.roles_list.insert(END, item)

        for i in reversed(selected_items):
            self.team_list.delete(i)

        self.update_display()

    def remove_all_from_team(self):
        if self.team_list.size() == 0:
            messagebox.showinfo("Информация", "Команда пуста")
            return

        all_roles = self.team_list.get(0, END)
        for role in all_roles:
            self.roles_list.insert(END, role)

        items = list(self.roles_list.get(0, END))
        items.sort()
        self.roles_list.delete(0, END)
        for item in items:
            self.roles_list.insert(END, item)

        self.team_list.delete(0, END)
        self.update_display()

    def restart_team(self):
        self.roles_list.delete(0, END)
        self.team_list.delete(0, END)
        self.load_available_members()

        self.update_display()
        messagebox.showinfo("Сброс", "Команда сформирована заново!")

    def update_display(self, event=None):
        available_total = self.roles_list.size()
        team_total = self.team_list.size()

        self.counter_display.config(
            text=f"Всего ролей: {available_total} | В команде: {team_total}"
        )


if __name__ == "__main__":
    main_window = tk.Tk()
    app = ProjectTeamSelector(main_window)
    main_window.mainloop()
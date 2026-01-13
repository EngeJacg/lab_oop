import tkinter as tk
import threading
import time

class MovingSquare(threading.Thread):
    def __init__(self, canvas_area, square_id, pos_x, pos_y, speed_x, speed_y):
        super().__init__(daemon=True)
        self.canvas_area = canvas_area
        self.square_id = square_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.active = True
        self.size = 30

    def run(self):
        while self.active:
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y

            if self.pos_x <= 30 or self.pos_x >= 470:
                self.speed_x = -self.speed_x
            if self.pos_y <= 30 or self.pos_y >= 370:
                self.speed_y = -self.speed_y

            self.canvas_area.coords(
                self.square_id,
                self.pos_x - self.size, self.pos_y - self.size,
                self.pos_x + self.size, self.pos_y + self.size
            )
            time.sleep(0.025)

class MultiThreadAnimation:
    def __init__(self, window):
        self.window = window
        self.window.title("Движущиеся квадраты")
        self.window.geometry("500x400")

        self.drawing_area = tk.Canvas(window, bg="#f0f8ff")
        self.drawing_area.pack(fill="both", expand=True)
        self.generate_squares()

    def generate_squares(self):
        square_colors = ["#ff6b6b", "#4ecdc4", "#45b7d1"]
        start_positions = [(100, 150), (250, 100), (400, 200)]
        velocity_pairs = [(2, 1), (-1, 2), (1, -2)]
        self.running_threads = []

        for idx in range(3):
            start_x, start_y = start_positions[idx]
            vel_x, vel_y = velocity_pairs[idx]

            square = self.drawing_area.create_rectangle(
                start_x - 30, start_y - 30, start_x + 30, start_y + 30,
                fill=square_colors[idx], outline="#2c3e50", width=3
            )

            thread_obj = MovingSquare(self.drawing_area, square, start_x, start_y, vel_x, vel_y)
            thread_obj.start()
            self.running_threads.append(thread_obj)

if __name__ == "__main__":
    main_window = tk.Tk()
    animation_app = MultiThreadAnimation(main_window)
    main_window.mainloop()
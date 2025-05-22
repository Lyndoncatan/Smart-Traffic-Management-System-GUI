import tkinter as tk
from tkinter import messagebox
import time
import threading

class SmartTrafficGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Traffic Management System Using Adaptive Signal Control")
        self.root.state('zoomed')
        self.root.resizable(True, True)

        self.vehicle_counts = {"North": 0, "South": 0, "East": 0, "West": 0}
        self.signal_lights = {}

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Smart Traffic Management System Using Adaptive Signal Control",
                 font=("Arial", 14, "bold"), fg="darkblue").pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.entries = {}
        for i, direction in enumerate(["North", "South", "East", "West"]):
            frame = tk.Frame(input_frame)
            frame.grid(row=i, column=0, pady=5)
            tk.Label(frame, text=f"{direction} Vehicles:", font=("Arial", 12)).pack(side=tk.LEFT)
            entry = tk.Entry(frame, width=10)
            entry.pack(side=tk.LEFT)
            self.entries[direction] = entry

        self.start_btn = tk.Button(self.root, text="Start Simulation", command=self.start_simulation,
                                   bg="green", fg="white", font=("Arial", 12))
        self.start_btn.pack(pady=15)

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(pady=10, expand=True, fill="both")

        self.root.bind("<Configure>", self.on_resize)

    def draw_intersection(self):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_x = width // 2
        center_y = height // 2
        road_width = 100

        # Draw roads
        self.canvas.create_rectangle(center_x - road_width // 2, 0, center_x + road_width // 2, height, fill="gray")
        self.canvas.create_rectangle(0, center_y - road_width // 2, width, center_y + road_width // 2, fill="gray")

        # Direction labels
        self.canvas.create_text(center_x, 20, text="North", font=("Arial", 10, "bold"))
        self.canvas.create_text(center_x, height - 20, text="South", font=("Arial", 10, "bold"))
        self.canvas.create_text(40, center_y, text="West", font=("Arial", 10, "bold"))
        self.canvas.create_text(width - 40, center_y, text="East", font=("Arial", 10, "bold"))

        # Draw traffic lights (Red, Orange, Green)
        positions = {
            "North": (center_x - 30, center_y - 150),
            "South": (center_x + 10, center_y + 110),
            "West":  (center_x - 150, center_y + 10),
            "East":  (center_x + 110, center_y - 30)
        }

        self.signal_lights.clear()
        for direction, (x, y) in positions.items():
            lights = [
                self.canvas.create_oval(x, y, x + 20, y + 20, fill="red"),
                self.canvas.create_oval(x, y + 25, x + 20, y + 45, fill="gray"),
                self.canvas.create_oval(x, y + 50, x + 20, y + 70, fill="gray")
            ]
            self.signal_lights[direction] = lights

    def on_resize(self, event):
        self.root.after(100, self.draw_intersection)

    def update_lights(self, active_direction):
        for direction, lights in self.signal_lights.items():
            self.canvas.itemconfig(lights[0], fill="red")
            self.canvas.itemconfig(lights[1], fill="gray")
            self.canvas.itemconfig(lights[2], fill="gray")

        lights = self.signal_lights[active_direction]
        self.canvas.itemconfig(lights[0], fill="gray")
        self.canvas.itemconfig(lights[2], fill="green")
        time.sleep(2)
        self.canvas.itemconfig(lights[2], fill="gray")
        self.canvas.itemconfig(lights[1], fill="orange")
        time.sleep(1)
        self.canvas.itemconfig(lights[1], fill="gray")
        self.canvas.itemconfig(lights[0], fill="red")

    def simulate_signal_cycle(self):
        cycle_order = sorted(self.vehicle_counts, key=self.vehicle_counts.get, reverse=True)
        for direction in cycle_order:
            self.update_lights(direction)
        self.start_btn.config(state=tk.NORMAL)

    def start_simulation(self):
        try:
            for dir in self.entries:
                self.vehicle_counts[dir] = int(self.entries[dir].get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integer values for all directions.")
            return

        self.start_btn.config(state=tk.DISABLED)
        threading.Thread(target=self.simulate_signal_cycle, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartTrafficGUI(root)
    root.mainloop()

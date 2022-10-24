import numpy as np
import tkinter as tk
from MapData import MapData
import threading
import time

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("geo-sim")
        self.canvas = tk.Canvas(self.root, height=30, width=30)
        self.canvas.pack()
        self.imageContainer = self.canvas.create_image(0,0)
        self.delay = 5 # Delay, for sim_loop, in seconds

        # -------- MapData -------- #

        population = MapData("maps/population.png", [1.0, 0.0, 0.0], 0, 10000)
        pop_rate = MapData("maps/pop_rate.png", [0.0, 1.0, 0.0], 0.9, 1.8)
        population.setModifiers(("*", [population, pop_rate]))
        self.maps = [population, pop_rate]

        # ------------------------- #
    
    def run(self):
        sim_thread = threading.Thread(target=self.sim_loop)
        draw_thread = threading.Thread(target=self.draw_loop)

        sim_thread.start()
        draw_thread.start()

    def draw_loop(self):
        while True:
            self.canvas.itemconfig(self.imageContainer, image=self.maps[0].TkImage)
            self.root.update_idletasks()
            self.root.update()
            time.sleep(0.1)

    def sim_loop(self):
        while True:
            time.sleep(self.delay)
            for map in self.maps:
                map.updateData()
            for map in self.maps:
                map.setDataToUpdated()

if __name__ == "__main__":
    app = App()
    app.run()
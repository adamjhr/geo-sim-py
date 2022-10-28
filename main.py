import numpy as np
import tkinter as tk
from MapData import MapData
from PIL import Image, ImageTk
import threading
import time

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("geo-sim")
        self.canvas = tk.Canvas(self.root, height=300, width=300)
        self.canvas.pack()
        self.pop_image = ImageTk.PhotoImage(Image.open("./maps/population.png").resize((300, 300), Image.NEAREST))
        self.imageContainer = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.pop_image)
        self.delay = 1 # Delay, for sim_loop, in seconds

        # -------- MapData -------- #

        population = MapData("maps/population.png", [1.0, 0.0, 0.0], 0, 10000)
        pop_rate = MapData("maps/pop_rate.png", [0.0, 1.0, 0.0], 0.9, 1.8)
        population.setModifiers(("*", [population, pop_rate]))
        self.maps = [population, pop_rate]

        # ------------------------- #
    
    def run(self):
        while True:
            for map in self.maps:
                map.updateData()
            for map in self.maps:
                map.setDataToUpdated()
            self.pop_image = ImageTk.PhotoImage(self.maps[0].image.resize((300, 300), Image.NEAREST))
            self.canvas.itemconfig(self.imageContainer, image=self.pop_image)
            self.root.update_idletasks()
            self.root.update()
            time.sleep(self.delay)

if __name__ == "__main__":
    app = App()
    app.run()
import tkinter as tk
from PIL import Image
from abc import ABC, abstractmethod

class MapData(ABC):

    def __init__(self, canvas: tk.Canvas, path, color, min, max):
        self.canvas = canvas
        self.min = min
        self.max = max        
        self.color = color
        self.image = Image.open(path)
        self.width = self.image.width
        self.height = self.image.height
        self.toCanvas = Image.new("RGB", (self.width, self.height))
        self.data = []

        # assert that canvas size fits image size

        self.populate_data_array()

        

    @abstractmethod
    def populate_data_array(self):
        pass

    def draw(self):
        


    def update(self):
        for x in range(self.width):
            for y in range(self.height):

                datapoint = data[]
                r = 255.0 * color[0]

                self.image.putpixel()

class ModifierData(MapData):
    
    def populate_data_array(self):
        return super().populate_data_array()

class AbsoluteData(MapData):
    
    def populate_data_array(self):

        baseImage = list(self.image.getdata())
        diff = self.max - self.min

        i = 0
        for value in baseImage:
            self.data[i] = ((value[0] / 255.0) * diff) + min
            i += 1
import tkinter as tk
from PIL import Image, ImageTk

class MapData:

    def __init__(self, path, color, max, min=0, updateMin=False):
        self.min = min
        self.max = max
        self.updateMin = updateMin
        self.color = color
        self.image = Image.open(path)
        self.width = self.image.width
        self.height = self.image.height
        self.image.resize((self.width*10, self.height*10), Image.NEAREST)
        self.data = []
        self.modifiers = []

        # assert that canvas size fits image size

        self.populate_data_array()
        self.dataUpdated = self.data


    def populate_data_array(self):
        baseImage = list(self.image.getdata())
        diff = self.max - self.min

        for value in baseImage:
            self.data.append(((value[0] / 255.0) * diff) + self.min)


    def updateImage(self):
        image = Image.new("RGB", (self.width, self.height))

        for i in range(len(self.data)):
            x = i % self.width
            y = i // self.width
            diff = self.max - self.min
            datapoint = (self.data[i] - self.max) / diff

            r = int(255.0 * self.color[0] * datapoint)
            g = int(255.0 * self.color[1] * datapoint)
            b = int(255.0 * self.color[2] * datapoint)

            image.putpixel((x, y), (r, g, b))

        image.resize((self.width*10, self.height*10), Image.NEAREST)

    def updateData(self):
        if self.modifiers != []:
            self.dataUpdated = self.combineData(self.modifiers)
            self.updateImage()

    def combineData(self, dataList):


        if not isinstance(dataList, tuple):
            return dataList.data

        returnList = []
        populated = False

        operation = dataList[0]
        match operation:
            case "+":
                for dataTuple in dataList[1]:
                    data = self.combineData(dataTuple)
                    if populated:
                        for i in range(len(data)):
                            returnList[i] += data[i]
                    elif not populated:
                        populated = True
                        for dataPiece in data:
                            returnList.append(dataPiece)
            case "*":
                for dataTuple in dataList[1]:
                    data = self.combineData(dataTuple)
                    if populated:
                        for i in range(len(data)):
                            returnList[i] *= data[i]
                    elif not populated:
                        populated = True
                        for dataPiece in data:
                            returnList.append(dataPiece)
        return returnList

    def setModifiers(self, modifiers):
        self.modifiers = modifiers

    def setDataToUpdated(self):
        self.data = self.dataUpdated
        for element in self.data:
            self.max = max(element, self.max)
            if (self.updateMin):
                self.min = min(element, self.min)

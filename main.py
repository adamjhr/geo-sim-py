import numpy as np
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("geo-sim")
    canvas = tk.Canvas(root, height=200, width=200)

    canvas.pack()
    root.mainloop()




if __name__ == "__main__":
    main()
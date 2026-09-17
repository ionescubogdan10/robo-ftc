import tkinter as tk
root = tk.Tk()
root.title("proiect robot")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
x=100;
y=100;
dimensiune = 150;
robot = canvas.create_rectangle(x, y, x+dimensiune, y+dimensiune, fill="white", outline="black", width=2)
root.mainloop()

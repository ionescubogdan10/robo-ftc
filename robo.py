import tkinter as tk
root = tk.Tk()
root.title("proiect robot")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
x=45
y=45
dimensiune = 45
viteza_x=2
viteza_y=2
canvas.create_rectangle(20, 20, 380, 380, fill="white", outline="black", width=2)
def miscare_robot():
    global x, y,viteza_x, viteza_y
    x += viteza_x
    y += viteza_y
    if x < 20 or x + dimensiune > 380:
        viteza_x = -viteza_x
    if y < 20 or y + dimensiune > 380:
        viteza_y = -viteza_y
    canvas.coords(robot, x, y, x+dimensiune, y+dimensiune)
    root.after(50, miscare_robot)
robot = canvas.create_rectangle(x, y, x+dimensiune, y+dimensiune, fill="blue", outline="black", width=2)
miscare_robot()
    
root.mainloop()

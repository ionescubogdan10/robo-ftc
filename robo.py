import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
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
tinta = canvas.create_rectangle(320, 320, 360, 360, fill="green")
nr_obstacole = simpledialog.askinteger("Input", "Introduceti numarul de obstacole (1-5):", minvalue=1, maxvalue=5)
obstacole = []
for i in range(nr_obstacole):
    x1 = simpledialog.askinteger("Input", f"Introduceti coordonata x a obstacolului {i+1} (20-380):", minvalue=20, maxvalue=380)
    y1 = simpledialog.askinteger("Input", f"Introduceti coordonata y a obstacolului {i+1} (20-380):", minvalue=20, maxvalue=380)
    x2 = x1 + 40
    y2 = y1 + 40
    obstacol = canvas.create_rectangle(x1, y1, x2, y2, fill="red")
    obstacole.append(obstacol)
def miscare_robot():
    global x, y,viteza_x, viteza_y
    x += viteza_x
    y += viteza_y
    if atingere_tinta():
        messagebox.showinfo("Felicitari!", "Robotul a atins tinta!")
        root.destroy()
        return
    if evitare_obstacole():
        viteza_x = -viteza_x
        viteza_y = -viteza_y
    if x < 20 or x + dimensiune > 380:
        viteza_x = -viteza_x
    if y < 20 or y + dimensiune > 380:
        viteza_y = -viteza_y
    canvas.coords(robot, x, y, x+dimensiune, y+dimensiune)
    root.after(50, miscare_robot)
def evitare_obstacole():
    elemente = canvas.find_overlapping(x, y, x+dimensiune, y+dimensiune)
    for elem in elemente:
        if elem in obstacole:
            return True
    return False
def atingere_tinta():
    elemente = canvas.find_overlapping(x, y, x+dimensiune, y+dimensiune)
    for elem in elemente:
        if elem == tinta:
            return True
    return False
def pixeli_grila(x, y):
    col = (x - 20) // 40
    rand = (y - 20) // 40
    return rand, col
def coordonate_grila(rand, col):
    x = 20 + col * 40
    y = 20 + rand * 40
    return x, y
def matrice_grila():
    matrice =  []
    for rand in range(9):
        rand_curent = []
        for col in range(9):
            x, y = coordonate_grila(rand, col)
            elemente = canvas.find_overlapping(x+5, y+5, x+35, y+35)
            if tinta in elemente:
                rand_curent.append("T")
            elif any(elem in obstacole for elem in elemente):
                rand_curent.append("O")
            else:
                rand_curent.append(".")
        matrice.append(rand_curent)
    return matrice 
def drum():
    matrice = matrice_grila()
    coada = [(0, 0)]
    parinte = {(0, 0): None}
    for rand, col in coada:
        if matrice[rand][col] == "T":
            rezultat = []
            curent = (rand, col)
            while curent is not None:
                rezultat.append(curent)
                curent = parinte[curent]
            return rezultat[::-1] 
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = rand + dr, col + dc
            if 0 <= r < 9 and 0 <= c < 9 and matrice[r][c] != "O":
                if (r, c) not in parinte:
                    parinte[(r, c)] = (rand, col)
                    coada.append((r, c)) # Îl punem la rând
                    
    return None
robot = canvas.create_rectangle(x, y, x+dimensiune, y+dimensiune, fill="blue", outline="black", width=2)
miscare_robot()
#harta = matrice_grila()
#for r in harta:
#    print(r)
root.mainloop()

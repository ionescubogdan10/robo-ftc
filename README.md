# robo-ftc
Simulare de navigare autonomă pentru un robot pe o grilă 9x9 folosind Tkinter și algoritmul BFS (Breadth-First Search).

## Despre proiect

Aplicația generează o grilă interactivă unde robotul calculează cel mai scurt drum de la punctul de start (0,0) până la țintă, evitând obstacolele din teren.

* **Algoritm:** BFS pentru garantarea celui mai scurt drum.
* **Interfață:** Tkinter (Canvas).
* **Mapare:** Conversie din coordonate ecran (pixeli) în matrice logică 9x9.

## Provocări tehnice și soluții

* **Sincronizarea interfeței cu logica:** Convertirea poziției reale a elementelor pe ecran (pixeli) într-o matrice de stare (`0`, `"O"`, `"T"`) a necesitat calcularea exactă a marginii și dimensiunii celulelor.
* **Reconstrucția traseului:** În algoritmul BFS, pentru a recupera drumul optim după ce ținta a fost găsită, a fost necesară parcurgerea înapoi a dicționarului de părinți și inversarea listei de coordonate.
* **Simularea mișcării:** Animarea robotului pe ecran fără a bloca interfața grafică s-a realizat prin actualizarea coordonatelor pas cu pas utilizând `root.update()` și întârzieri controlate.

  * **Coliziuni la colțuri:** Robotul atingea vizual marginea obstacolelor în timpul ocolirii. Soluția a fost ajustarea corectă a dimensiunii Sprite-ului și calcularea strictă a celulelor ocupate în matrice.
* **Viteza de deplasare:** Inițial, robotul se mișca prea repede pe ecran. Am adăugat o pauză între pași (`root.after(1000)`) pentru a crea o animație fluidă și ușor de urmărit.
* **Blocarea în start (Edge Case):** Se putea plasa un obstacol direct peste poziția inițială a robotului (0,0), ceea ce oprea simularea instant. Am rezolvat ridicand limita minima de input la y la 70 in loc de 20.

## Rulare

Necesită Python 3.

```bash
python robo.py

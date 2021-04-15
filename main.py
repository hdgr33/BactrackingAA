import random
from tkinter import *
import tkinter as tk
import time

Answer = []
Clues = []
Suspects = ["El mejor amigo", "La novia", "La vecina", "El mensajero", "El extrano", "El hermanastro", "La colega"]
Weapon = ["La pistola", "El cuchillo", "El machete", "La pala", "El bate", "La botella", "El tubo ", "La cuerda"]
Motive = ["Venganza", "Celos", "Dinero", "Accidente", "Drogas", "Robo"]
Body_Part = ["Cabeza", "Pecho", "Abdomen", "Espalda", "Piernas", "Brazos"]
Place = ["Sala", "Comedor", "Baño", "Terraza", "Cuarto", "Garage", "Patio", "Balcón", "Cocina"]


def find_clues():
    global Clues
    global Answer
    used = []
    Clues = []
    cont=0
    while len(Clues) < 2:
        x = random.randint(1, 5)
        if x == 1 and x not in used:
            clue = Suspects[random.randint(0, 6)]
            if clue not in Answer:
                Clues.append(clue)
                used.append(x)
            if clue in Answer and cont==0:
                cont+=1
                Clues.append(clue)
                used.append(x)
        elif x == 2 and x not in used:
            clue = Weapon[random.randint(0, 7)]
            if clue not in Answer:
                Clues.append(clue)
                used.append(x)
            if clue in Answer and cont==0:
                cont+=1
                Clues.append(clue)
                used.append(x)
        elif x == 3 and x not in used:
            clue = Motive[random.randint(0, 5)]
            if clue not in Answer:
                Clues.append(clue)
                used.append(x)
            if clue in Answer and cont==0:
                cont+=1
                Clues.append(clue)
                used.append(x)
        elif x == 4 and x not in used:
            clue = Body_Part[random.randint(0, 5)]
            if clue not in Answer:
                Clues.append(clue)
                used.append(x)
            if clue in Answer and cont==0:
                cont+=1
                Clues.append(clue)
                used.append(x)
        elif x == 5 and x not in used:
            clue = Place[random.randint(0, 8)]
            if clue not in Answer:
                Clues.append(clue)
                used.append(x)
            if clue in Answer and cont==0:
                cont+=1
                Clues.append(clue)
                used.append(x)
    print(Clues)
    Cl.insert(tk.END, str(Clues) + '\n')
    return Clues


def find_solution():
    global Suspects
    global Weapon
    global Motive
    global Body_Part
    global Place
    global Answer
    global Clues
    Answer = []
    x = random.randint(0, len(Suspects) - 1)
    Answer.append(Suspects[x])
    x = random.randint(0, len(Weapon) - 1)
    Answer.append(Weapon[x])
    x = random.randint(0, len(Motive) - 1)
    Answer.append(Motive[x])
    x = random.randint(0, len(Body_Part) - 1)
    Answer.append(Body_Part[x])
    x = random.randint(0, len(Place) - 1)
    Answer.append(Place[x])
    print(Answer)
    clues = find_clues()
    print(clues, "clues")
    return Answer


def validate(res):
    global Answer
    y = 0
    if res != Answer:

        print(res, Answer)
        while y < 5:
            print(y)
            if res[y] != Answer[y]:
                print('esta mal')
                return y
            else:
                y += 1
    elif y == 5:
        print('todo mal')
    else:
        print("respuesta correct")
        return 8


def validate2(res):
    global Answer
    y = []
    if res != Answer:

        print(res, Answer)

        while len(y) < 5:
            x = random.randint(0, 4)
            if res[x] != Answer[x]:
                print(res[x], Answer[x])
                print('carta incorrecta')
                if x not in y:
                    y.append(x)
                return x
    elif y == 5:
        print('todo mal')
    else:
        print("respuesta correct")
        return 8


def brute():
    time1 = time.perf_counter()
    global Suspects
    global Weapon
    global Motive
    global Body_Part
    global Place
    global Answer
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    while True:
        res = validate2([Suspects[i], Weapon[j], Motive[k], Body_Part[l], Place[m]])
        T.insert(tk.END, str([Suspects[i], Weapon[j], Motive[k], Body_Part[l], Place[m]]) + '\n')
        if res == 0:
            i += 1
        elif res == 1:
            j += 1
        elif res == 2:
            k += 1
        elif res == 3:
            l += 1
        elif res == 4:
            m += 1
        elif res == 8:
            time2 = time.perf_counter()
            time3 = time2 - time1
            T.insert(tk.END, "tiempo total =" + str(time3) + '\n')
            return False


def backtrack():
    time1 = time.perf_counter()
    global Suspects
    global Weapon
    global Motive
    global Body_Part
    global Place
    global Answer
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    armaRes(i, j, k, l, m)
    time2 = time.perf_counter()
    time3 = time2 - time1
    Bc.insert(tk.END, "tiempo total =" + str(time3) + '\n')


def armaRes(i, j, k, l, m):
    res = vigilaExcepciones([Suspects[i], Weapon[j], Motive[k], Body_Part[l], Place[m]])
    if res == True:
        res = validate2([Suspects[i], Weapon[j], Motive[k], Body_Part[l], Place[m]])
        Bc.insert(tk.END, str([Suspects[i], Weapon[j], Motive[k], Body_Part[l], Place[m]]) + '\n')
    if res == 0:
        i += 1
    elif res == 1:
        j += 1
    elif res == 2:
        k += 1
    elif res == 3:
        l += 1
    elif res == 4:
        m += 1
    elif res == 8:
        return False
    return armaRes(i, j, k, l, m)


def vigilaExcepciones(res):
    print(res)
    global Clues
    control = 0
    for i in range(0, 5):
        if res[i] in Clues:
            control += 1
        if control >= 2:
            return i
    return True


def pictureSolution():
    global Answer
    for i in range(0, 5):
        if i == 0:
            if Answer[i] == "El mejor amigo":
                iconCulpable.config(image=amigo)
            elif Answer[i] == "La novia":
                iconCulpable.config(image=novia)
            elif Answer[i] == "La vecina":
                iconCulpable.config(image=vecina)
            elif Answer[i] == "El mensajero":
                iconCulpable.config(image=mensajero)
            elif Answer[i] == "El extrano":
                iconCulpable.config(image=extrano)
            elif Answer[i] == "El hermanastro":
                iconCulpable.config(image=hermanastro)
            elif Answer[i] == "La colega":
                iconCulpable.config(image=colega)
        elif i == 1:
            print(Answer, i)
            if Answer[i] == "La pistola":
                iconArma.config(image=pistola)
            elif Answer[i] == "El cuchillo":
                iconArma.config(image=cuchillo)
            elif Answer[i] == "El machete":
                iconArma.config(image=espada)
            elif Answer[i] == "La pala":
                iconArma.config(image=pala)
            elif Answer[i] == "El bate":
                iconArma.config(image=bate)
            elif Answer[i] == "La botella":
                iconArma.config(image=botella)
            elif Answer[i] == "El tubo":
                iconArma.config(image=tuberia)
            elif Answer[i] == "La cuerda":
                iconArma.config(image=cuerda)
        elif i == 2:
            if Answer[i] == "Venganza":
                iconMotivo.config(image=venganza)
            elif Answer[i] == "Celos":
                iconMotivo.config(image=celos)
            elif Answer[i] == "Dinero":
                iconMotivo.config(image=dinero)
            elif Answer[i] == "Accidente":
                iconMotivo.config(image=accidente)
            elif Answer[i] == "Drogas":
                iconMotivo.config(image=drogas)
            elif Answer[i] == "Robo":
                iconMotivo.config(image=robo)
        elif i == 3:
            if Answer[i] == "Cabeza":
                iconCuerpo.config(image=cabeza)
            elif Answer[i] == "Pecho":
                iconCuerpo.config(image=pecho)
            elif Answer[i] == "Abdomen":
                iconCuerpo.config(image=abdomen)
            elif Answer[i] == "Espalda":
                iconCuerpo.config(image=espalda)
            elif Answer[i] == "Piernas":
                iconCuerpo.config(image=pierna)
            elif Answer[i] == "Brazos":
                iconCuerpo.config(image=brazo)
        elif i == 4:
            print(Answer[i])
            if Answer[i] == "Sala":
                iconLugar.config(image=sala)
            elif Answer[i] == "Comedor":
                iconLugar.config(image=comedor)
            elif Answer[i] == "Baño":
                iconLugar.config(image=bano)
            elif Answer[i] == "Terraza":
                iconLugar.config(image=terraza)
            elif Answer[i] == "Cuarto":
                iconLugar.config(image=cuarto)
            elif Answer[i] == "Garage":
                iconLugar.config(image=garaje)
            elif Answer[i] == "Patio":
                iconLugar.config(image=patio)
            elif Answer[i] == "Balcón":
                iconLugar.config(image=balcon)
            elif Answer[i] == "Cocina":
                iconLugar.config(image=cocina)


ventana = Tk()
ventana.title("2048")
ALTO = 690
ANCHO = 1320
anchoPantalla = ventana.winfo_screenwidth()
largoPantalla = ventana.winfo_screenheight()
POS_VENTANA_X = int((anchoPantalla / 2) - (ANCHO / 2))
POS_VENTANA_Y = int((largoPantalla / 2) - (ALTO / 2))
ventana.geometry("{}x{}+{}+{}".format(ANCHO, ALTO, POS_VENTANA_X, POS_VENTANA_Y))
ventana.resizable(FALSE, FALSE)
marco = Frame(ventana, bg="green", width=1320, height=770, highlightthickness=0)
marco.place(x=0, y=0)
fondoimagen = PhotoImage(file="red.png")
estructura = Canvas(marco, width=1320, height=770, bg="yellow", highlightthickness=0)
estructura.place(relx=0.5, rely=0.5, anchor=CENTER)
fondo = Label(estructura)
fondo.place(relx=0.5, rely=0.45, anchor=CENTER)
fondo.config(image=fondoimagen)
T = Text(estructura, height=6, width=50, bg="white", font=("Elephant", "14"))
T.place(relx=0.01, rely=0.45)
Bc = Text(estructura, height=6, width=50, bg="white", font=("Elephant", "14"))
Bc.place(relx=0.01, rely=0.66)
Cl = Text(estructura, height=3, width=10, bg="white", font=("Elephant", "14"))
Cl.place(relx=0.7, rely=0.48)
mistery = PhotoImage(file="Diapositiva37.png")
mensajero = PhotoImage(file="Diapositiva1.PNG")
vecina = PhotoImage(file="Diapositiva2.PNG")
hermanastro = PhotoImage(file="Diapositiva3.PNG")
novia = PhotoImage(file="Diapositiva4.PNG")
colega = PhotoImage(file="Diapositiva5.PNG")
extrano = PhotoImage(file="Diapositiva6.PNG")
amigo = PhotoImage(file="Diapositiva7.PNG")
cuchillo = PhotoImage(file="Diapositiva8.PNG")
bate = PhotoImage(file="Diapositiva9.PNG")
cuerda = PhotoImage(file="Diapositiva10.PNG")
tuberia = PhotoImage(file="Diapositiva11.PNG")
botella = PhotoImage(file="Diapositiva12.PNG")
pala = PhotoImage(file="Diapositiva13.PNG")
espada = PhotoImage(file="Diapositiva14.PNG")
pistola = PhotoImage(file="Diapositiva15.PNG")
sala = PhotoImage(file="Diapositiva16.PNG")
terraza = PhotoImage(file="Diapositiva17.PNG")
patio = PhotoImage(file="Diapositiva18.PNG")
garaje = PhotoImage(file="Diapositiva19.PNG")
cuarto = PhotoImage(file="Diapositiva20.PNG")
balcon = PhotoImage(file="Diapositiva21.PNG")
bano = PhotoImage(file="Diapositiva22.PNG")
comedor = PhotoImage(file="Diapositiva23.PNG")
cocina = PhotoImage(file="Diapositiva24.PNG")
cabeza = PhotoImage(file="Diapositiva25.PNG")
brazo = PhotoImage(file="Diapositiva26.PNG")
pierna = PhotoImage(file="Diapositiva27.PNG")
espalda = PhotoImage(file="Diapositiva28.PNG")
abdomen = PhotoImage(file="Diapositiva29.PNG")
pecho = PhotoImage(file="Diapositiva30.PNG")
celos = PhotoImage(file="Diapositiva31.PNG")
accidente = PhotoImage(file="Diapositiva32.PNG")
venganza = PhotoImage(file="Diapositiva33.PNG")
robo = PhotoImage(file="Diapositiva34.PNG")
drogas = PhotoImage(file="Diapositiva35.PNG")
dinero = PhotoImage(file="Diapositiva36.PNG")
cargar = Button(estructura, command=find_solution, text="Generar Solucion", font=("Elephant", "10"), bg="white")
cargar.place(relx=0.70, rely=0.65, anchor=CENTER)
dibujar = Button(estructura, command=pictureSolution, text="Ensenar Cartas", font=("Elephant", "10"), bg="white")
dibujar.place(relx=0.80, rely=0.65, anchor=CENTER)
fuerzaBruta = Button(estructura, command=brute, text="Ensenar Brute", font=("Elephant", "10"), bg="white")
fuerzaBruta.place(relx=0.90, rely=0.65, anchor=CENTER)
back = Button(estructura, command=backtrack, text="Ensenar Backtrack", font=("Elephant", "10"), bg="white")
back.place(relx=0.90, rely=0.75, anchor=CENTER)
rest = Button(estructura, command=find_clues, text="Seleccionar restricciones", font=("Elephant", "10"), bg="white")
rest.place(relx=0.70, rely=0.75, anchor=CENTER)
cartaCulpable = Canvas(marco, width=227, height=302, bg="white", highlightthickness=0)
cartaCulpable.place(relx=0.1, rely=0.21, anchor=CENTER)
iconCulpable = Label(cartaCulpable, bg="white")
iconCulpable.place(x=0, y=0)
iconCulpable.config(image=mistery)
cartaArma = Canvas(marco, width=227, height=302, bg="white", highlightthickness=0)
cartaArma.place(relx=0.3, rely=0.21, anchor=CENTER)
iconArma = Label(cartaArma, bg="white")
iconArma.place(x=0, y=0)
iconArma.config(image=mistery)
cartaMotivo = Canvas(marco, width=227, height=302, bg="white", highlightthickness=0)
cartaMotivo.place(relx=0.5, rely=0.21, anchor=CENTER)
iconMotivo = Label(cartaMotivo, bg="white")
iconMotivo.place(x=0, y=0)
iconMotivo.config(image=mistery)
cartaCuerpo = Canvas(marco, width=227, height=302, bg="white", highlightthickness=0)
cartaCuerpo.place(relx=0.7, rely=0.21, anchor=CENTER)
iconCuerpo = Label(cartaCuerpo, bg="white")
iconCuerpo.place(x=0, y=0)
iconCuerpo.config(image=mistery)
cartaLugar = Canvas(marco, width=227, height=302, bg="white", highlightthickness=0)
cartaLugar.place(relx=0.9, rely=0.21, anchor=CENTER)
iconLugar = Label(cartaLugar, bg="white")
iconLugar.place(x=0, y=0)
iconLugar.config(image=mistery)
# x = find_solution()


ventana.mainloop()

if __name__ == '__main__':
    find_solution()
#   brute()
#    validate2(['La novia', 'La pala', 'Accidente', 'Pecho', 'Cocina'])

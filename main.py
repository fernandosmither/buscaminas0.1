import random
import tkinter
from tkinter.constants import DISABLED, NORMAL

#region FUNCIONES

def abrir_casilla(mapa, coords, boton, idmina): # coords -> [fila,columna] ((NO DARLOS VUELTA!!)) EL C INDICA LA ID DEL BOTON
    global dimension
    fila = int(coords[0])
    columna = int(coords[1])
    # if boton['state'] == NORMAL:
    #     boton['state'] = DISABLED
    if mapa[fila][columna][0] == 0: #Caso 0, flood fill
        print(f"Debug: Abrir_casilla -> Inicio flood_fill")
        return flood_fill(mapa, coords, boton, idmina)
    elif mapa[fila][columna][0] == 'X': #Caso 'X', mina y game_over. (dar opción para crear nuevo mapa)
        mapa[fila][columna][2] = 1#Marcamos la mina para poner en fondo rojo
        return game_over(mapa)
    else:   #Caso número distinto de 0, no bomba. Apertura única. ((Posibles errores.))
        mapa[fila][columna][2] = 1
        return cambiar_icono(mapa, coords, boton, idmina)

    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # for fila in mapa:
    #     print(fila)
    print("Ciclo abrir_casilla terminado")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # print(f"Ejecutado: [columna : {columna}, fila : {fila}]")
    print(f"Coords: {coords}")


def flood_fill(mapa, coords, boton, idmina):#Usar segunda propiedad de pos como checkeo de visited. Utilizar flood fill 2d para 4 direcciones. N-S-E-O
    global dimension #Otra wea posiblemente ilegal. Cuidado
    global botones #wey ya

    coords[0] = int(coords[0])
    coords[1] = int(coords[1])
    fila = coords[0]
    columna = coords[1]


    idmina = int(coords[0])+int(coords[1])*dimension
    print(f"Flood_fill: Ahora revisando coords: {coords}, con un idmina: {idmina}")
    
    if fila >= dimension or columna >= dimension:
        # print("Pos supera a dimension, skipping")
        # if fila >= dimension and columna >= dimension:
        #     coords[0] -= 1
        #     fila -= 1
        #     coords[1] -= 1
        #     columna -= 1
        # elif fila >= dimension:
        #     coords[0] -= 1
        #     fila -= 1
        # elif columna >= dimension:
        #     coords[1] -= 1
        #     columna -= 1
        return "Pos supera a dimension, skipping"

    if fila < 0 or columna < 0:
        # print("Pos menor a 0, skipping")
        # if fila < 0 and columna < 0:
        #     coords[0] += 1
        #     fila += 1
        #     print("Sume uno a la fila")
        #     coords[1] += 1
        #     columna += 1
        #     print(f"Sume uno a la columna: {columna}")
        # if fila < 0:
        #     coords[0] += 1
        #     fila += 1
        #     print("Sume uno a la fila")
        # elif columna < 0:
        #     coords[1] += 1
        #     columna += 1
        #     print(f"Sume uno a la columna: {columna}")
        return "Pos menor a 0, skipping"
    
    if idmina >= dimension**2 or idmina < 0:
        print(f'ID de boton "c" se pasa. ID: {idmina}')
        return 'ID de boton "c" se pasa. Skipping!'
    boton = botones[idmina]


    if mapa[fila][columna][1] != 'default':
        print("Ya visitado, skipping")
        print(f"Coords: {coords}")
        return "Ya visitado, skipping"
    mapa[fila][columna][1] = 'visited'

    # if mapa[fila][columna][0] != 'X' and mapa[fila][columna][0] != 0:
    if mapa[fila][columna][0] != 0:
        return abrir_casilla(mapa, coords, boton, idmina)

    elif mapa[fila][columna][0] == 0:
        print("Ejecucion #1")
        # print(f"Constancia. El c de ahora es {c} y le restaremos la dimension {dimension}")
        cambiar_icono(mapa, coords, boton, idmina)
        flood_fill(mapa, coords, boton, idmina)


    print(f"Coords a modificar: {coords}")
    coords[1] -= 1
    flood_fill(mapa, coords, boton, idmina)

    coords[0] += 1
    flood_fill(mapa, coords, boton, idmina)

    coords[1] += 1
    flood_fill(mapa, coords, boton, idmina)

    coords[1] += 1
    flood_fill(mapa, coords, boton, idmina)

    coords[0] -= 1
    flood_fill(mapa, coords, boton, idmina)

    coords[0] -= 1
    flood_fill(mapa, coords, boton, idmina)

    coords[1] -= 1
    flood_fill(mapa, coords, boton, idmina)

    coords[1] -= 1
    flood_fill(mapa, coords, boton, idmina)

    coords[0] += 1
    coords[1] += 1
    

def click_derecho(texto): #manejo de bandera/cruz
    # boton.config(image=bandera_img)
    print(texto)

def game_over(mapa):
    global botones
    global dimension#Esto en teoría es ilegalisimo. Arreglar

    i = 0
    for x in range(dimension):
        for y in range(dimension):
            botonaedit = botones[i]
            cambiar_icono(mapa, [ y, x ], botonaedit, i)
            i += 1

    print("Game over~")
    #

def cambiar_icono(mapa, coords, boton, idmina):
    fila = int(coords[0])
    columna = int(coords[1])

    if mapa[fila][columna][0] == 1:
        boton["image"] = uno_img

    elif mapa[fila][columna][0] == 2:
        boton["image"] = dos_img
    
    elif mapa[fila][columna][0] == 3:
        boton["image"] = tres_img
    
    elif mapa[fila][columna][0] == 4:
        boton["image"] = cuatro_img
    
    elif mapa[fila][columna][0] == 5:
        boton["image"] = cinco_img
    
    elif mapa[fila][columna][0] == 6:
        boton["image"] = seis_img
    
    elif mapa[fila][columna][0] == 7:
        boton["image"] = siete_img
    
    elif mapa[fila][columna][0] == 8:
        boton["image"] = ocho_img
    
    elif mapa[fila][columna][0] == 0:
        boton["image"] = marcado_img
    
    elif mapa[fila][columna][0] == 'X' and mapa[fila][columna][2] == 0:
        boton["image"] = minagris_img

    elif mapa[fila][columna][0] == 'X' and mapa[fila][columna][2] == 1:
        boton["image"] = minaroja_img


#endregion


#region CONFIG y variables
dimension = 8
minas = 10

#Recursos
ventana = tkinter.Tk()
default_img = tkinter.PhotoImage(file = r"files\default.png")
default_img = default_img.subsample(30, 30)
bandera_img = tkinter.PhotoImage(file = r"files\bandera.png")
bandera_img = bandera_img.subsample(30, 30)
interrogacion_img = tkinter.PhotoImage(file = r"files\interrogacion.png")
interrogacion_img = interrogacion_img.subsample(30, 30)
marcado_img = tkinter.PhotoImage(file = r"files\marcado.png")
marcado_img = marcado_img.subsample(30, 30)
minagris_img = tkinter.PhotoImage(file = r"files\minagris.png")
minagris_img = minagris_img.subsample(30, 30)
minaroja_img = tkinter.PhotoImage(file = r"files\minaroja.png")
minaroja_img = minaroja_img.subsample(30, 30)
uno_img = tkinter.PhotoImage(file = r"files\1.png")
uno_img = uno_img.subsample(30, 30)
dos_img = tkinter.PhotoImage(file = r"files\2.png")
dos_img = dos_img.subsample(30, 30)
tres_img = tkinter.PhotoImage(file = r"files\3.png")
tres_img = tres_img.subsample(30, 30)
cuatro_img = tkinter.PhotoImage(file = r"files\4.png")
cuatro_img = cuatro_img.subsample(30, 30)
cinco_img = tkinter.PhotoImage(file = r"files\5.png")
cinco_img = cinco_img.subsample(30, 30)
seis_img = tkinter.PhotoImage(file = r"files\6.png")
seis_img = seis_img.subsample(30, 30)
siete_img = tkinter.PhotoImage(file = r"files\7.png")
siete_img = siete_img.subsample(30, 30)
ocho_img = tkinter.PhotoImage(file = r"files\8.png")
ocho_img = ocho_img.subsample(30, 30)


#endregion

#region CREACION TABLERO Y RNG
####Formato de celda: [VALOR {'X'/número {0,8}} , MARCADO {"default"/"bandera"/"cruz"}, PULSADO {0/1}]
tablero = [[] for i in range(dimension)]
for i in range(len(tablero)):
    tablero[i] = [ ["inicio", "default", 0] for z in range(dimension)]

#Colocamos las bombas en orden
fila_actual = 0
columna_actual = 0
for i in range(minas):
    if fila_actual == dimension-1 and columna_actual == dimension-1:
        print(f"ERROR 1 en creación de tablero, bombas excede máximo")
        exit()
    if tablero[fila_actual][columna_actual][0] == 'inicio':
        tablero[fila_actual][columna_actual][0] = 'X'
    else:
        columna_actual += 1

    if columna_actual == dimension:
        fila_actual += 1
        columna_actual = 0
    
    tablero[fila_actual][columna_actual][0] = 'X'

tablero_shuffling = []
for i in range(len(tablero)):
    tablero_shuffling += tablero[i]

random.shuffle(tablero_shuffling)

tablero = []
iter = 0
for i in range(dimension):
    tablero.append( tablero_shuffling[ iter : dimension*(i+1) ] )
    iter = dimension*(i+1)



#Insertamos los números

for fila in range(dimension):
    for columna in range(dimension):
        if tablero[fila][columna][0] == "inicio":
            adyacencia = 0

            if fila == 0: #Primera fila
                if columna == 0: #Primera columna. Caso [0,0]
                    if tablero[fila][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna][0] == 'X':
                        adyacencia += 1

                elif columna == dimension - 1: #Ultima columna
                    if tablero[fila][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna][0] == 'X':
                        adyacencia += 1

                else:# Columnas al medio, primera fila
                    if tablero[fila][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila][columna + 1][0] == 'X':
                        adyacencia += 1

            elif fila == dimension-1: #Ultima fila
                if columna == 0: #Ultima fila, primera columna, caso [ultima, 0]
                    if tablero[fila - 1][columna][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila][columna + 1][0] == 'X':
                        adyacencia += 1

                elif columna == dimension-1: #Ultima fila, ultima columna, caso [ultima, ultima]
                    if tablero[fila - 1][columna][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila][columna - 1][0] == 'X':
                        adyacencia += 1

                else: #Columnas al medio, ultima fila
                    if tablero[fila][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila][columna + 1][0] == 'X':
                        adyacencia += 1

            else:#filas de al medio
                if columna == 0: #Primera columna, filas de al medio, caso [0,-x-]
                    if tablero[fila - 1][columna][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna][0] == 'X':
                        adyacencia += 1

                elif columna == dimension-1: #Ultima columna, filas de al medio, caso [0,-x-]
                    if tablero[fila - 1][columna][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna][0] == 'X':
                        adyacencia += 1

                else: #Columnas de al medio, filas de al medio, caso [-x-, -y-]
                    if tablero[fila][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna + 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna][0] == 'X':
                        adyacencia += 1
                    if tablero[fila - 1][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna - 1][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna][0] == 'X':
                        adyacencia += 1
                    if tablero[fila + 1][columna + 1][0] == 'X':
                        adyacencia += 1
            tablero[fila][columna][0] = adyacencia

#endregion

for fila in tablero:
    print(fila)


#region GUI (ventana)
ventana.geometry("600x600")

numeros = []
botones = []
for x in range(dimension):
    for y in range(dimension):
        numeros.append([x,y])

i = 0
for x in range(dimension):
    for y in range(dimension):
        boton = tkinter.Button(ventana, width = 30, height = 30, text=f"{x},{y}", image = default_img, command=lambda c=i: abrir_casilla(tablero, [ botones[c].cget("text").split(",")[1], botones[c].cget("text").split(",")[0] ], botones[c], c) )
        # boton.bind('<Button-3>', click_derecho(boton.cget("text")))  # bind right mouse click
        boton.grid(column = x, row = y)
        print(f"i: {i}")
        i += 1
        botones.append(boton)



ventana.mainloop()


#endregion


# for fila in tablero:
#     print(fila)

# coords = input()
# coords = coords.split(",")

# abrir_casilla(tablero, coords)

# for fila in tablero:
#     print(fila)

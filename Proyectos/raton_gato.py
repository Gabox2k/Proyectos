#Bloque1
#importar lo aleatorio
import random


comida_queso=0
num_quesos= 8
filas, columnas = 10, 10
num_obstaculo= 5


#Tabla vacio
tablero = [["[]" for _ in range(columnas)] for _ in range(filas)]

# Coordenadas para el gato y el raton
gato  = (9, 3)   # 🐱
raton= [0 ,1]

#Coordenas dentro del tablero
tablero[gato[0]][gato[1]]   = "🐱"

#Bloque 2
quesos = set ()
obstaculo = set()

# Aletorio del obstaculo y queso 
while len(obstaculo) < num_obstaculo:
    obsta= (random.randint(0, filas -1), random.randint(0, columnas-1))
    
    
    if obsta != (gato) and obsta != tuple(raton) and  obsta not in (obstaculo):
        obstaculo.add(obsta)
        tablero[obsta[0]][obsta[1]] = "🧱"


while len(quesos) < num_quesos:
    queso = (random.randint(0, filas - 1), random.randint(0, columnas - 1))
    
    if queso != (gato) and queso != tuple(raton) and queso not in (quesos) and queso not in (obstaculo):
        quesos.add(queso)
        tablero[queso[0]][queso[1]] = "🧀"
        
    
#Bloque 3
#posicion del raton
def mostrar_tablero():
    for i in range(filas):        
        for j in range(columnas):   
            if [i, j] == raton and (i , j )  == gato:
                print ("🐱",end = " ")
            elif [i, j] == raton:
                print("🐭", end=" ")
            elif [i,j] == gato:
                print("🐱", end=" ")
            else:                   
                print(tablero[i][j], end=" ")  
        print()                     
    print()                         



#Distacia dx y dy
def distancia(x,y):
   dis = abs (x[0] - y[0]) +  abs(x[1] - y[1]) 
   return dis if dis != 0 else -100
    
#Bloque 4  
#Posibles del raton
def posibles_raton(posicion):
    movimiento = [ (posicion[0] -1, posicion[1]),
                   (posicion[0] +1, posicion[1]),
                   (posicion[0], posicion[1] -1),
                   (posicion[0], posicion[1] +1)]
    
    #Para que el raton no salga del tablero y pase los mueros
    return [
        movimi for movimi in movimiento
        if 0 <= movimi[0] < filas and 0 <= movimi[1] < columnas and movimi not in obstaculo
    ]

#Posibles del gato
def posibles_gato(posicion):
    movimiento = [(posicion[0] -1, posicion[1]),
                  (posicion[0] +1, posicion[1]),
                  (posicion[0], posicion[1] -1),
                  (posicion[0], posicion[1] +1)]


#El gato pueda saltar los muros
    if comida_queso >= 4:
        return[
        movimi for movimi in movimiento
        if 0<= movimi[0] < filas and 0 <= movimi[1] < columnas 
    ]
    else:
        #Para que el gato no salga del tablero y pase los mueros
        return[
            movimi for movimi in movimiento
            if 0<= movimi[0] < filas and 0 <= movimi[1] < columnas and movimi not in obstaculo
        ]
    
    
    
    
    
#Bloque 5
#funcion con el minimax 
def Minimax (posibili_gato, posibili_raton, profundidad, max_turno):
    if profundidad == 0 or posibili_gato == tuple(raton):
        return -distancia(posibili_gato, posibili_raton), posibili_gato
    
    if max_turno:
        mejor_val = float("-inf")
        mejor_movi = posibili_gato
        for movi in posibles_gato(posibili_gato):
            valor, _ = Minimax(movi, posibili_raton, profundidad -1 , False)
            if valor > mejor_val:
                mejor_val = valor
                mejor_movi = movi
        return mejor_val, mejor_movi
    else:
        mejor_val = float ("inf")
        mejor_movi = posibili_raton
        for movi in posibles_raton(posibili_raton):
            valor ,_ = Minimax(posibili_gato, movi, profundidad -1, True)
            if valor < mejor_val:
                mejor_val = valor
                mejor_movi = movi
        return mejor_val , mejor_movi
  
  

  
#Bloque 6
#Movimientos del gato
def mov_gato():
    global gato
    _, mejor_mov = Minimax(gato, raton, profundidad=3, max_turno=True)
                 
    if comida_queso < 4 and mejor_mov in obstaculo:
        print(" ")
                  
            
    if (gato [0], gato[1]) in quesos:    
        tablero[gato[0]] [gato[1]] = "🧀"
    elif (gato[0], gato[1]) in obstaculo:
        tablero[gato[0]] [gato[1]] = "🧱"
    else:
        tablero[gato[0]] [gato[1]] = "[]"

    gato = mejor_mov
    tablero[gato[0]] [gato[1]] = "🐱"


#Bloque 7
nue_fila = raton[0] 
nue_columna = raton[1]

#Para que el raton se mueva
while True:
    mostrar_tablero()
    print("arriba:w  abajo:s  iquz:a  dere:d       Escribir: Salir para salir del juego")
    tecla = input("Mover: ")
    #Para dejar de ejecutar el juego
    if  tecla == "Salir":
        break
    
    #Movimientos del raton
    if tecla == "w":
        nue_fila = raton[0] - 1
        nue_columna = raton[1]
    elif tecla == "s":
        nue_fila = raton[0] + 1
        nue_columna = raton[1]
    elif tecla == "a":
        nue_fila = raton[0]
        nue_columna = raton[1] - 1
    elif tecla == "d":
        nue_fila = raton[0]
        nue_columna = raton[1] + 1
    #Raton se mueve de forma diagonal
    elif comida_queso >= 4 and tecla == "q":
        nue_fila = raton[0] -1
        nue_columna = raton[1] -1 
    elif comida_queso >= 4 and tecla == "e":
        nue_fila = raton[0] -1
        nue_columna = raton[1] +1
    elif comida_queso >= 4 and tecla == "z":
        nue_fila = raton[0] +1
        nue_columna = raton[1] -1 
    elif comida_queso >= 4 and tecla == "c":
        nue_fila = raton[0] +1
        nue_columna = raton [1] +1
    else:
        print("Tecla no válida")
        continue
    
    
    print(f"Nueva posicion del raton: " , nue_fila, nue_columna)
    
    #Bloque 8 
    #Para que coma queso 
    if 0 <= nue_fila < filas and 0 <= nue_columna < columnas \
       and (nue_fila, nue_columna) not in obstaculo \
       and (nue_fila, nue_columna) != gato:
        raton[0], raton[1] = nue_fila, nue_columna

        if (nue_fila, nue_columna) in quesos:
            quesos.remove((nue_fila , nue_columna))
            tablero[nue_fila][nue_columna] = "[]"
            comida_queso +=1
            
            if comida_queso == 4:
                print("Has desbloqueado los movimientos diagonales")
                print("diagonal izqu:q digonal dere: e  diagonal abajo izqu: z diagonal abajo dere: c")
        else:
            if comida_queso < 4:
                print("Movimientos diagonales bloqueados")
        mov_gato()
        if gato == tuple(raton):
            mostrar_tablero()
            print ("El gato te atrapo")
            break
        
        if not quesos:
                mostrar_tablero()
                print("Has ganado")
                break
            
            

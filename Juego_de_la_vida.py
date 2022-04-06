import time
from copy import deepcopy
import numpy as np
tamano_matriz_alto = 10
tamano_matriz_largo = 10

#Primer tamaño de matriz 10x10
matriz_juego_vida = [['~','#','~','#','~','#','#','#','#','#'],
 	 ['#','~','~','~','~','~','#','#','#','#'],
 	 ['~','~','~','~','~','~','~','~','#','#'],
 	 ['#','#','~','~','#','~','#','~','~','~'],
 	 ['~','#','~','~','~','~','~','~','~','~'],
 	 ['~','~','~','#','#','~','#','~','#','~'],
 	 ['~','~','~','~','~','#','~','~','~','~'],
 	 ['~','~','~','~','~','~','~','#','~','~'],
 	 ['#','#','~','~','#','~','~','~','#','#'],
 	 ['#','#','#','#','#','~','~','~','#','~']]

#Segundo tamaño de matriz 5x5
matriz_juego_vida2 = [['~','#','~','#','~'],
 	 ['~','~','~','#','~'],
 	 ['#','#','~','#','~'],
 	 ['#','#','~','#','~'],
 	 ['~','~','#','~','~'],]

#Tercero tamaño de matriz 15x15
matriz_juego_vida3 = [['~','#','~','#','~','#','#','#','#','#','~','#','~','#','#'],
 	 ['~','#','~','#','~','#','~','~','#','~','~','#','~','#','~'],
 	 ['~','~','~','#','~','#','~','#','~','~','~','~','~','~','#'],
 	 ['~','~','~','~','~','~','~','~','~','#','~','#','~','#','#'],
 	 ['~','#','~','#','#','#','~','#','~','#','~','~','~','#','~'],
 	 ['~','~','~','~','~','~','#','~','~','~','~','#','~','~','~'],
 	 ['~','#','~','#','~','#','~','#','#','#','~','~','~','~','#'],
 	 ['~','#','~','#','#','#','~','~','#','~','~','~','#','~','~'],
 	 ['~','~','~','~','~','~','#','~','~','#','~','#','~','#','~'],
 	 ['~','#','~','#','~','#','~','~','#','~','~','#','~','#','~'],
   ['~','#','~','#','#','~','~','~','~','~','~','~','~','~','~'],
   ['~','#','#','#','#','#','#','~','#','~','~','#','~','#','~'],
   ['~','#','~','#','~','~','~','~','#','~','~','#','~','~','~'],
   ['~','#','~','~','~','#','~','~','#','~','~','~','~','#','~'],
   ['~','#','~','#','~','~','#','~','~','~','~','#','~','~','~']]

def imprimir_matriz_juego_vida(matriz_a_imprimir):
  for i in matriz_a_imprimir:
    print(i)
  print("")

#En posicion vamos a mandar (fila,columna)
def checando_vecinos(matriz_juego_vida, posicion):
  vecinos_vivos = 0
  #Checando la posición (0,0)
  if posicion ==(0,0):
    for i in matriz_juego_vida[0:2]:
      for j in i[0:2]:
        if(j == '#'):
          vecinos_vivos += 1
  #Checando el punto inferior izquierdo de la matriz (tamano_matriz_alto-1,0)
  elif posicion == (tamano_matriz_alto-1,0):
    for i in matriz_juego_vida[tamano_matriz_alto-2:tamano_matriz_alto]:
      for j in i[0:2]:
        if(j == '#'):
          vecinos_vivos += 1
  
  #Checando el punto superior derecho de la matriz (0,tamano_matriz_largo-1)
  elif posicion == (0,tamano_matriz_largo-1):
    for i in matriz_juego_vida[0:2]:
      for j in i[tamano_matriz_largo-2:tamano_matriz_largo]:
        if(j == '#'):
          vecinos_vivos += 1

  #Checando el punto inferior derecho de la matriz (tamano_matriz_alto-1,tamano_matriz_largo-1)
  elif posicion == (tamano_matriz_alto-1,tamano_matriz_largo-1):
    for i in matriz_juego_vida[tamano_matriz_alto-2:tamano_matriz_alto]:
      for j in i[tamano_matriz_largo-2:tamano_matriz_largo]:
        if(j == '#'):
          vecinos_vivos += 1

  #Checando los puntos que estan en el lado izquierdo de la matriz (x,0)   
  elif posicion[1]==0 :
    for i in matriz_juego_vida[posicion[0]-1:posicion[0]+2]:
      for j in i[0:2]:
        if(j == '#'):
          vecinos_vivos += 1
  #Checando los puntos que estan en el lado superior de la matriz (0,x)   
  elif posicion[0]==0 :
    for i in matriz_juego_vida[0:2]:
      for j in i[posicion[1]-1:posicion[1]+2]:
        if(j == '#'):
          vecinos_vivos += 1
  #Checando los puntos que estan en el lado derecho de la matriz (x,9)   
  elif posicion[1]==tamano_matriz_largo-1:
    for i in matriz_juego_vida[posicion[0]-1:posicion[0]+2]:
      for j in i[tamano_matriz_largo-2:tamano_matriz_largo]:
        if(j == '#'):
          vecinos_vivos += 1
  #Checando los puntos que estan en el lado inferior de la matriz (9,x)   
  elif posicion[0]==tamano_matriz_alto-1:
    for i in matriz_juego_vida[tamano_matriz_alto-2:tamano_matriz_alto]:
      for j in i[posicion[1]-1:posicion[1]+2]:
        if(j == '#'):
          vecinos_vivos += 1
  #Checando cualquier otro punto
  else:
    for i in matriz_juego_vida[posicion[0]-1:posicion[0]+2]:
      for j in i[posicion[1]-1:posicion[1]+2]:
        if(j == '#'):
          vecinos_vivos += 1
  
  #Si el elemento que estamos analizando es igual a # (viva) lo quitamos del numero de vecinos vivos
  if (matriz_juego_vida[posicion[0]][posicion[1]] =='#'):
    vecinos_vivos -= 1
  return vecinos_vivos

def matriz_nueva(matriz_juego_vida):
  #Imprimimos la matriz actual
  imprimir_matriz_juego_vida(matriz_juego_vida)
  time.sleep(3)
  #Creamos una matriz nueva del mismo tamaño, la cual sera llenada con la nueva información
  matriz_modificada = deepcopy(matriz_juego_vida)
  for i in range(tamano_matriz_alto):
    for j in range(tamano_matriz_largo):
      numero_vecinos_vivos = checando_vecinos(matriz_juego_vida,(i,j))
      #Si la celula esta viva
      if matriz_juego_vida[i][j] == '#':
        #Si tiene 2 o 3 celulas cerca, continua viva
        if numero_vecinos_vivos == 2 or numero_vecinos_vivos == 3:
          matriz_modificada[i][j]='#'
        #Si no,muere
        else:
          matriz_modificada[i][j]='~'
      #Si esta muerta la celula
      elif matriz_juego_vida[i][j]=='~':
        if numero_vecinos_vivos == 3:
          matriz_modificada[i][j]='#'
        else:
          matriz_modificada[i][j]='~' 
  #Volvemos a llamar la función para ver la evolución de las celulas
  matriz_nueva(matriz_modificada)

#Iniciamos el programa
matriz_nueva(matriz_juego_vida)



  

import pygame
from sys import stdin 

## aqui se lee el texto mk de deelan la matriz ya sea hecha o no hecha 
def leershit():
    with open("maze.txt") as f:
        array = []
        line = f.readline().strip() 
        while(line):
            array.append(list(line))
            line = f.readline().strip()
    print(array,"la pinche matriz")
    return array
lista=leershit()

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255) ## esta mierda es el espacio vacio 0
COLORDEELAN = ( 200, 200, 200) ## esta mierda es la pared  #
ROJO = (255, 0, 0) ## esta mierda es el inicio    B
OTROC= (0,0,255) ## Otro color que no se es para punto de interes  +
OTROC2=(255,0,255)## Otro color cacorro para el final E
# Establecemos el LARGO y ALTO de cada celda de la retícula.
LARGO  = 10
ALTO = 10
 
# Establecemos el margen entre las celdas.
MARGEN = 5
 
# Creamos un array bidimensional. Un array bidimensional
# no es más que una lista de listas.
grid = []
for fila in range(120):
    # Añadimos un array vacío que contendrá cada celda 
    # en esta fila
    grid.append([])
    for columna in range(120):
        grid[fila].append(0) # Añade una celda
 
# Establecemos la fila 1, celda 5 a uno. (Recuerda, los números de las filas y
# columnas empiezan en cero.)
grid[1][5] = 1
 
# Inicializamos pygame
pygame.init()
  
# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [1780,1780]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
 
# Establecemos el título de la pantalla.
pygame.display.set_caption("A * de la PUJ")
 
# Iteramos hasta que el usuario pulse el botón de salir.
hecho = False
 
# Lo usamos para establecer cuán rápido de refresca la pantalla.
reloj = pygame.time.Clock()
 
# -------- Bucle Principal del Programa-----------
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
        # elif evento.type == pygame.MOUSEBUTTONDOWN:
        #     # El usuario presiona el ratón. Obtiene su posición.
        #     pos = pygame.mouse.get_pos()
        #     print(pos,"esta es la puta pos de la pantalla")
        #     # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
        #     columna = pos[0] // (LARGO + MARGEN)
        #     fila = pos[1] // (ALTO + MARGEN)
        #     # Establece esa ubicación a cero
        #     grid[fila][columna] = 1
        #     print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
 
    # Establecemos el fondo de pantalla.
    pantalla.fill(NEGRO)
 
    # Dibujamos la retícula para las dos AQUI VA LA CONCHA ESA QUE HAY QUE CAMBIAR PARA PINTAR 
    for fila in range(120):
        for columna in range(120):
            color = BLANCO
            if lista[fila][columna] == "#":
                color = NEGRO
            if lista[fila][columna] == "0":
                color = BLANCO
            if lista[fila][columna] == "B":
                color = ROJO
            if lista[fila][columna] == "+":
                color = OTROC
            if lista[fila][columna] == "E":
                color = OTROC2
            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN+LARGO) * columna + MARGEN,
                              (MARGEN+ALTO) * fila + MARGEN,
                              LARGO,
                              ALTO])
     
    # Limitamos a 60 fotogramas por segundo.
    reloj.tick(60)
 
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
     
# Pórtate bien con el IDLE.

pygame.quit()

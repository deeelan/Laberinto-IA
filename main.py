import pygame as pygame
from sys import stdin
from pygame.locals import *

## asi se pintan numeros
"""   
numero1 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('1',True,(0,0,200)), (100,200))

numero2 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('2',True,(0,0,200)), (100,200))

numero3 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('3',True,(0,0,200)), (100,200))

numero4 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('4',True,(0,0,200)), (100,200))

numero5 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('5',True,(0,0,200)), (100,200))

numero6 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('6',True,(0,0,200)), (100,200))

numero7 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('7',True,(0,0,200)), (100,200))

numero8 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('8',True,(0,0,200)), (100,200))

numero9 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('9',True,(0,0,200)), (100,200))

numero0= pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('0',True,(0,0,200)), (100,200))
"""  


class Cell:
    """
        Clase celda que describe si es pared, visitada, inicio, fin, punto de interes y puntaje. Esto para el algoritmo A*
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isWall = False
        self.visited = False
        self.isEnd = False
        self.isBegin = False
        self.isSpot = False
        self.score = -1

    def __str__(self):
        if(self.isWall):
            return 'W'
        elif(self.isEnd):
            return 'E'
        elif(self.isBegin):
            return 'B'
        elif(self.isSpot):
            return '@'
        else:
            return ' '

class Maze():
    def getInitialMatrix(self):
        """
            Método que dada una matriz con las referencias descritas abajo, lo carga a nuestra clase celda
            
            La matriz es un archivo txt donde:
                # : pared
                0 : espacio vacio
                + : punto de interes
                B : inicio
                E : fin
        """       
        inp = open("src/maze test.txt", 'r')
        matrix = []
        for line in inp:
            matrix.append(list(line.replace('\n', '')))
        inp.close()

        return matrix

    
    def generateEmptyMaze(self, matrix):
        """
            Metodo que genera la matriz de la clase Cell (sin scores)
        """
        for y in range(0, len(matrix)):
            row = []
            for x in range(0, len(matrix[y])):
                cell = Cell(x, y)
                cell.visited = False;

                char = matrix[y][x]

                if(char == '#'):
                    cell.isWall = True;
                    cell.score = 0;

                if(char == '0'):
                    cell.score = 0;

                if(char == '+'):
                    cell.score = '100'
                    cell.isSpot = True

                if(char == 'B'):
                    cell.isBegin = True;
                    cell.score = -1;

                if(char == 'E'):
                    cell.isEnd = True;
                    cell.score = 1000;

                row.append(cell);
            self.grid.append(row);

        # strin = ''
        # for row in self.grid:
        #     for celda in row:
        #         strin += str(celda)
        #     strin += '\n'
        # print(strin)

    def __init__(self):
        matrix = self.getInitialMatrix();
        self.grid = []
        self.generateEmptyMaze(matrix)

    def display(self):
        # Definimos algunos colores
        NEGRO = (0, 0, 0)
        BLANCO = (255, 255, 255) ## esta mierda es el espacio vacio 0
        COLORDEELAN = ( 255, 255, 0) ## esta mierda es la pared  #
        ROJO = (255, 0, 0) ## esta mierda es el inicio    B
        OTROC= (0,0,255) ## Otro color que no se es para punto de interes  +
        OTROC2=(255,0,255)## Otro color cacorro para el final E
        # Establecemos el LARGO y ALTO de cada celda de la retícula.
        LARGO  = 20
        ALTO = 20
         
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
         
        # Inicializamos pygame
        pygame.init()
        pygame.font.init()
          
        # Establecemos el LARGO y ALTO de la pantalla
        DIMENSION_VENTANA = [1180,1780]
        pantalla = pygame.display.set_mode((DIMENSION_VENTANA),pygame.RESIZABLE)
         
        # Establecemos el título de la pantalla.
        pygame.display.set_caption("A * de la PUJ made by Deelan and Caliche")
         
        # Iteramos hasta que el usuario pulse el botón de salir.
        hecho = False
         
        # Lo usamos para establecer cuán rápido de refresca la pantalla.
        reloj = pygame.time.Clock()

        self.font = pygame.font.SysFont('Arial', 25)
         
        # -------- Bucle Principal del Programa-----------
        while not hecho:
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT: 
                    hecho = True
            # Establecemos el fondo de pantalla.
            pantalla.fill(NEGRO)

            # Dibujamos la retícula para las dos AQUI VA LA CONCHA ESA QUE HAY QUE CAMBIAR PARA PINTAR

            for fila in self.grid:
                #print(self.grid,"la cosa de deelan")
                for celda in fila:
                    color = BLANCO
                    if celda.isWall==True:
                        color = NEGRO
                    if celda.isSpot ==True:
                        color = COLORDEELAN ### no pinta
                    if celda.isBegin ==True:
                        color = ROJO
                    if celda.visited ==True:
                        color = OTROC
                    if celda.isEnd ==True:
                        color = OTROC2
                    pygame.draw.rect(pantalla,
                                     color,
                                     [(MARGEN+LARGO) * celda.x + MARGEN,
                                      (MARGEN+ALTO) * celda.y + MARGEN,
                                      LARGO,
                                      ALTO])
                    font = pygame.font.SysFont('Arial', 15)
                    #if len(str(celda.score))>3:
                        #str(celda.score)[0:3]
                        #print("Corto",celda.score)
                    pantalla.blit(font.render(str(celda.score)[0:3],True,(0,0,200)), [(MARGEN+LARGO) * celda.x + MARGEN,
                                      (MARGEN+ALTO) * celda.y + MARGEN,
                                      LARGO,
                                      ALTO])
            # Limitamos a 60 fotogramas por segundo.
            reloj.tick(60)
         
            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()
             
        # Pórtate bien con el IDLE.

        pygame.quit()




def main():
    m = Maze()
    m.display()

main()
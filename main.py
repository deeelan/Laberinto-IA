import pygame

posX = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
posY = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

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
            return f'W : {self.score}'
        elif(self.isEnd):
            return f'E : {self.score}'
        elif(self.isBegin):
            return f'B : {self.score}'
        elif(self.isSpot):
            return f'@ : {self.score}'
        else:
            return f'  : {self.score}'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

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
        for x in range(0, len(matrix)):
            row = []
            for y in range(0, len(matrix[x])):
                cell = Cell(x, y)
                cell.visited = False;

                char = matrix[x][y]

                if(char == '#'):
                    cell.isWall = True;
                    cell.score = 0;

                if(char == '0'):
                    cell.score = 1;

                if(char == '+'):
                    cell.score = 100
                    cell.isSpot = True

                if(char == 'B'):
                    cell.isBegin = True;
                    cell.score = 0;
                    self.initx = x
                    self.inity = y

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
        self.initx = 0
        self.inity = 0
        self.path = []
        self.generateEmptyMaze(matrix)

    def deelanEuristhic(self):
        for i in range(1, len(self.grid) - 2):
            for j in range(1, len(self.grid[i]) - 2):
                if(not self.grid[i][j].visited):
                    tCell = self.grid[i][j];

                    tCell.visited = True;

                    summ = 0
                    for x in range(9):
                        #print(self.grid[i - posX[x]][j - posY[x]])
                        summ += self.grid[i - posX[x]][j - posY[x]].score

                    tCell.score = 1 / (summ / 9)

                    self.grid[i][j] = tCell;


    def setScores(self, euristhic):
        if(euristhic == 'deelan'):
            self.deelanEuristhic();
        else:
            print('Euristhic function doesnt exists')

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
          
        # Establecemos el LARGO y ALTO de la pantalla
        DIMENSION_VENTANA = [1780,1780]
        pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
         
        # Establecemos el título de la pantalla.
        pygame.display.set_caption("A * de la PUJ made by Deelan and Caliche")
         
        # Iteramos hasta que el usuario pulse el botón de salir.
        hecho = False
         
        # Lo usamos para establecer cuán rápido de refresca la pantalla.
        reloj = pygame.time.Clock()
         
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
             
            # Limitamos a 60 fotogramas por segundo.
            reloj.tick(60)
         
            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()
             
        # Pórtate bien con el IDLE.
        pygame.quit()

    def solve(self, algorithm, euristhic):
        self.setScores(euristhic)

        if(algorithm == "astar"):
            self.aStar();
        else:
            print("Algorithm not implemented yet")

    def aStar(self):
        start_node = self.grid[self.initx][self.inity]
        #start_node.visited = True

        openList = []
        closedList = []
        openList.append(start_node)

        while(len(openList) > 0):
            current_node = openList[0]

            index = 0
            for i in range(len(openList)):
                if(openList[i].score < current_node.score):
                    index = i
                    current_node = openList[i]
            
            openList.pop(index)
            current_node.visited = True
            self.path.append(current_node)
            closedList.append(current_node)

            #print(f"is end? {current_node.isEnd}")
            if(current_node.isEnd):
                return
            
            children = []

            for i in range(9):
                #print(f"in pos ({current_node.x}, {current_node.y})")
                #print(f"pivot in pos ({current_node.x - posX[i]}, {current_node.y - posY[i]})")
                node_pivot = self.grid[current_node.x - posX[i]][current_node.y - posY[i]]

                #print(f"node_pivot >>> {node_pivot}")

                #print(f"is not wall ? {not node_pivot.isWall}")
                if(not node_pivot.isWall):
                    children.append(node_pivot)

            print(f"children >>> {children}")

            for child in children:
                for closed_child in closedList:
                    if(child == closed_child):
                        continue

                child.score += current_node.score

                for open_child in openList:
                    if(child == open_child):
                        continue

                openList.append(child)

            #print(openList)
            #print(closedList)

        for cell in self.path:
            print(cell)


def main():
    m = Maze()
    #m.display()

    m.solve('astar', 'deelan')
    m.display()


main()
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
        inp = open("src/maze.txt", 'r')
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



def main():
    m = Maze()

main()
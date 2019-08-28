from mazelib import Maze
from mazelib.generate.Prims import Prims

m = Maze()
m.generator = Prims(60, 60)
m.generate()
print(m)
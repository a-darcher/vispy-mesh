import numpy as np
from mesh import Mesh
from vispy import app, gloo
np.set_printoptions(suppress=True, precision=2)

#Import mesh
monkey = Mesh('monkey.obj', position=[10,2,3], rotation=[90,45,0], scale=[2,2,2])
print(monkey.model_matrix)
print(monkey.position)

# Make Window
canvas = app.Canvas(keys='interactive')



@canvas.connect # modifier, which lets following function be used more broadly
def on_draw(event): #event manager
	gloo.clear([.2,.4,0])
	canvas.update()
	

# Show window, Run Program 

canvas.show()
app.run()

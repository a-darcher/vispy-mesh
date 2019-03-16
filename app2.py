import numpy as np
from mesh import Mesh
from vispy import app, gloo
np.set_printoptions(suppress=True, precision=2)

#all of this is only to define gl_Position
VERT_SHADER = """
attribute vec3 vertex; 
void main(){
	gl_Position = vec4(vertex, 1.);
}
"""

FRAG_SHADER = """
void main(){
	gl_FragColor = vec4(1., 0., 0., 1.);
}
"""

program = gloo.Program(VERT_SHADER, FRAG_SHADER)

#Import mesh
monkey = Mesh('monkey.obj', position=[10,2,3], rotation=[90,45,0], scale=[2,2,2])
print(monkey.model_matrix)
print(monkey.position)

attributes = [
	('vertex',np.float32,3)
]

data = np.zeros(len(monkey.vertices), attributes) #strutured array to preallocate memory
data['vertex'] = monkey.vertices 	
print(data)
vertex_buffer = gloo.VertexBuffer(data)
program.bind(vertex_buffer) # sends vertices over to the graphics card, so card has pool of vertices to work with

index_buffer = gloo.IndexBuffer(monkey.faces)
# Make Window
canvas = app.Canvas(keys='interactive')



@canvas.connect # modifier, which lets following function be used more broadly
def on_draw(event): #event manager
	gloo.clear([.2,.4,0])
	program.draw('triangles', index_buffer)	
	canvas.update()
	

# Show window, Run Program 

canvas.show()
app.run()

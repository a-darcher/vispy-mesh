from vispy.util import transforms as tr
from vispy import io
import numpy as np

np.set_printoptions(suppress=True, precision=2)

class Mesh:
	def __init__(self, obj_filename, position, rotation, scale):
		vertices, faces, normals, texcoords = io.read_mesh(obj_filename)
		assert len(vertices[0]) == 3, "Vertices incompatible"
		assert len(faces[0]) == 3, "Mesh must be triangulated"	
		self.vertices = vertices - np.mean(vertices, axis=0)
		self.faces = faces
		self.position = position
		self.rotation = rotation
		self.scale = scale	
		
	

	@property	
	def model_matrix(self):
		"""
		returns 4x4 model matrix from translation, rotation, and data data 	
		""" 
		sm = tr.scale(self.scale).T 
		rx,ry,rz = self.rotation 
		rzm = tr.rotate(rz, [0,0,1]).T 
		rym = tr.rotate(ry, [0,1,0]).T 
		rxm = tr.rotate(rx, [1,0,0]).T 
		trm = tr.translate(self.position).T 
		mm = trm @ rxm @ rym @ rzm @ sm  
		return mm 
	


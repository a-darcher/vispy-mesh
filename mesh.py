from vispy.util import transforms as tr
import numpy as np

np.set_printoptions(suppress=True, precision=2)

def make_model_matrix(translate, rotation, scale): 
	"""
	returns 4x4 model matrix from translation, rotation, and data data 	
	""" 
    sm = tr.scale(scale).T 
    rx,ry,rz = rotation 
    rzm = tr.rotate(rz, [0,0,1]).T 
    rym = tr.rotate(ry, [0,1,0]).T 
    rxm = tr.rotate(rx, [1,0,0]).T 
    trm = tr.translate(translate).T 
    mm = trm @ rxm @ rym @ rzm @ sm  
    return mm 

mm = model_matrix = make_model_matrix([1,2,3], [90,45,0], [2,2,2])
print(mm)

print('change')



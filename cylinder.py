import numpy as np
from exportToPly import write_ply_file

pointPerRing = 8
nbRing = 3

vertices = []
faces = []

for i in range (nbRing) :
  for j in range (pointPerRing) :
    phi = j * (2*np.pi/pointPerRing)
    x=np.cos(phi)
    y=np.sin(phi)
    z= float(i)
    vertices.append([x,y,z])
vertices = np.array(vertices)
    
for i in range(nbRing - 1):
    for j in range(pointPerRing):
        # Índices dos vértices no anel inferior (i)
        v_baixo = i * pointPerRing + j
        v_baixo_prox = i * pointPerRing + ((j + 1) % pointPerRing)

        # Índices dos vértices no anel superior (i + 1)
        v_cima = (i + 1) * pointPerRing + j
        v_cima_prox = (i + 1) * pointPerRing + ((j + 1) % pointPerRing)

        # Primeiro triângulo do quadrilátero
        faces.append([v_baixo, v_baixo_prox, v_cima_prox])

        # Segundo triângulo do quadrilátero
        faces.append([v_baixo, v_cima_prox, v_cima])

faces = np.array(faces)

write_ply_file(vertices, faces, 'cylinder.ply' )
	

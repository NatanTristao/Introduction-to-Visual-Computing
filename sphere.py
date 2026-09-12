import numpy as np
from exportToPly import write_ply_file

pointPerRing = 8
nbRing = 8
radius = 1.0

vertices = []

for i in range (nbRing) :
  for j in range (pointPerRing) :
    theta = i*(np.pi/(nbRing - 1))
    phi = j*(2*np.pi/pointPerRing)
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    vertices.append([x,y,z])
vertices = np.array(vertices)

faces = []

# O loop de faces vai de i = 0 ate nbRing - 2 (para conectar i com i+1)
for i in range(nbRing - 1):
    for j in range(pointPerRing):
        # Indices dos vertices no anel atual (i)
        v_baixo = i * pointPerRing + j
        v_baixo_prox = i * pointPerRing + ((j + 1) % pointPerRing)

        # Indices dos vertices no anel seguinte (i + 1)
        v_cima = (i + 1) * pointPerRing + j
        v_cima_prox = (i + 1) * pointPerRing + ((j + 1) % pointPerRing)

        # Se NAO estivermos no Polo Norte, adiciona o primeiro triangulo
        if i != 0:
            faces.append([v_baixo, v_cima_prox ,v_baixo_prox, ])

        # Se NAO estivermos no Polo Sul, adiciona o segundo triangulo
        if i != nbRing - 2:
            faces.append([v_baixo, v_cima ,v_cima_prox, ])

faces = np.array(faces)

write_ply_file(vertices, faces, 'sphere.ply')

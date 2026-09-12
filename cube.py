import numpy as np
from exportToPly import write_ply_file

vertices = np.array([
  [0.0,0.0,0.0], #0
  [1.0,0.0,0.0], #1
  [0.0,1.0,0.0], #2
  [1.0,1.0,0.0], #3
  [0.0,0.0,1.0], #4
  [1.0,0.0,1.0], #5
  [0.0,1.0,1.0], #6
  [1.0,1.0,1.0], #7
])

cube = np.array([
    #z=0
  [0, 2, 1],
  [1, 2, 3],

  #z=1
  [4, 5, 6],
  [5, 7, 6], 

  #x=0
  [0, 4, 2],
  [6, 2, 4],

  #x=1
  [1, 3, 5],
  [3, 7, 5],

  #y=0
  [0, 1, 4],
  [1, 5, 4],

  #y=1
  [2, 6, 3],
  [3, 6, 7]
], dtype=int)

write_ply_file(vertices,cube, 'cube.ply' )
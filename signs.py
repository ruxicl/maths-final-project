import numpy as np

def count_cut_vertices():
    
    isCutVertex = [True] * 8

    for i in range(8):
        for j in range(i + 1, 8):
            # if the vertices i and j are connected and they have the same sign, then neither of them is a cut vertex
            if edges[i][j] and new_signs[i] == new_signs[j]:
                isCutVertex[i] = False
                isCutVertex[j] = False 

    # return the number of cut vertices in the current octant
    return sum(isCutVertex)



# Choice of triangulation

# standard triangulation
edges = [[True, True, False, True, True, False, False, False],
         [True, True, True, True, True, True, False, True],
         [False, True, True, True, False, True, True, True],
         [True, True, True, True, True, False, False, True],
         [True, True, False, True, True, True, False, True],
         [False, True, True, False, True, True, True, True],
         [False, False, True, False, False, True, True, True],
         [False, True, True, True, True, True, True, True]]

# Choice of signs for the unit cube
signs = np.zeros(8)
for i in range(8):
    sign = int(input())
    signs[i] = sign

total_cut_vertices = 0

# Count of cut vertices in the first octant

# Define reflections across xy, yz, and xz planes
xyrefl = np.array([-1, -1, -1, -1, 1, 1, 1, 1])
yzrefl = np.array([-1, 1, 1, -1, -1, 1, 1, -1])
xzrefl = np.array([-1, -1, 1, 1, -1, -1, 1, 1])

reflections = [yzrefl, xzrefl, xyrefl]

new_signs = signs

print("Number of cut vertices in")
for reflacrossxy in [True, False]:
    for reflacrossyz in [True, False]:
        for reflacrossxz in [True, False]:
            octant=''
            new_signs = np.copy(signs)
            for (i, reflacross) in enumerate([reflacrossyz, reflacrossxz, reflacrossxy]):
                if reflacross:
                    new_signs = np.multiply(new_signs, reflections[i])
                    octant += '-'
                else:
                    octant += '+'
            nr_cut_vertices = count_cut_vertices()
            print ("Octant", octant, ": ", nr_cut_vertices)
            total_cut_vertices += nr_cut_vertices

print("Total: ", total_cut_vertices)

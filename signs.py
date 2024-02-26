import numpy as np
import itertools

def count_cut_vertices_current_octant(new_signs):
    
    isCutVertex = [True] * 8

    for i in range(8):
        for j in range(i + 1, 8):
            # if the vertices i and j are connected and they have the same sign, then neither of them is a cut vertex
            if edges[i][j] and new_signs[i] == new_signs[j]:
                isCutVertex[i] = False
                isCutVertex[j] = False 

    # return the number of cut vertices in the current octant
    return sum(isCutVertex)

def count_total_nr_cut_vertices(signs, per_octant):

    # Define reflections across xy, yz, and xz planes
    xyrefl = np.array([-1, -1, -1, -1, 1, 1, 1, 1])
    yzrefl = np.array([-1, 1, 1, -1, -1, 1, 1, -1])
    xzrefl = np.array([-1, -1, 1, 1, -1, -1, 1, 1])

    reflections = [yzrefl, xzrefl, xyrefl]

    total_cut_vertices = 0

    if per_octant:
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
                nr_cut_vertices = count_cut_vertices_current_octant(new_signs)

                if per_octant:
                    print ("Octant", octant, ": ", nr_cut_vertices)

                total_cut_vertices += nr_cut_vertices

    print("Total: ", total_cut_vertices)

    return total_cut_vertices

# Find a sign distribution that produces the maximum number of cut vertices 
def find_max_sign_distr():
    max_cut_vertices = 0
    max_sign_distr = []
    # Generate all possible sign distributions
    for vertex_signs in itertools.product([-1, 1], repeat=8):
        sign_distr = np.asarray(vertex_signs)
        total_cut_vertices = count_total_nr_cut_vertices(sign_distr)
        if (total_cut_vertices > max_cut_vertices):
            max_cut_vertices = total_cut_vertices
            max_sign_distr = [sign_distr]
        elif (total_cut_vertices == max_cut_vertices):
            max_sign_distr.append(sign_distr)
    
    print ("Maximum number of cut vertices is ", max_cut_vertices)
    print ("This can be achieved with the following sign distribution(s)")
    for i in range(len(max_sign_distr)):
        print(max_sign_distr[i])


# Choice of triangulation

# standard triangulation
std_triang = [[True, True, False, True, True, False, False, False],
         [True, True, True, True, True, True, False, True],
         [False, True, True, True, False, True, True, True],
         [True, True, True, True, True, False, False, True],
         [True, True, False, True, True, True, False, True],
         [False, True, True, False, True, True, True, True],
         [False, False, True, False, False, True, True, True],
         [False, True, True, True, True, True, True, True]]

#  to do: triang as user input? (but with no guarantee that the triangulation is convex)


edges = std_triang

# Choice of signs for the unit cube
user_signs = np.zeros(8)
for i in range(8):
    sign = int(input())
    user_signs[i] = sign

count_total_nr_cut_vertices(user_signs, per_octant=True)

# find_max_sign_distr()

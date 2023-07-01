def get_F(cube):

    F = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    for key in cube.keys():

        ro = cube[key][0]
        mu = cube[key][1]
        F[key] = ro / mu

    return F

def get_V(cube):
    pass
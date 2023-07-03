import numpy as np

def get_r(a, cx, cy):

    i = np.indices(a.shape)
    ix = (i[0, :, :] - cx) ** 2
    iy = (i[1, :, :] - cy) ** 2
    r = np.sqrt(ix + iy)

    return r


# Funcion para calcular el factor de calibracion F(lambda)
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

# Funcion para calcular el polinomio viñeta V(x,y)
def get_V(cube):

    V = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [],  
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    for key in cube.keys():

        a = np.ones((cube[key][2]['Width'], cube[key][2]['Height']))
        cx, cy = cube[key][2]['Vcenter']

        r = get_r(a, cx, cy)

        k = [float(k_) for k_ in (cube[key][2]['Vpoly'])]

        den = 1 + k[0]*r + k[1]*r**2 + k[2]*r**3 + k[3]*r**4 + k[4]*r**5 + k[5]*r**6

        V[key] = 1 / den

    return V

def get_Rv(cube):

    Rv = {'Blue-444'    : [], 'Blue'    : [], 
          'Green-531'   : [], 'Green'   : [], 
          'Red-650'     : [], 'Red'     : [], 
          'Red edge-705': [], 'NIR'     : [], 
          'Red edge-740': [], 'Red Edge': []
    }

    for key in cube.keys():

        print(cube[key][2].keys())

        _, a2, a3 = cube[key][2]['RadioCal']
        Te = cube[key][2]['Te']

        den = np.array([1 + (a2*y/Te) - (a3*y) for y in range(cube[key][2]['Height'])])

        Rv[key] = 1 / den

    return Rv

def correct_im(cube, ims):

    I = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    for key in ims.keys():

        bl = cube[key][2]['BL']

        I[key] = ims[key] - bl

    return I



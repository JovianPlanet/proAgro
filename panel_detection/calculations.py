import numpy as np
import cv2
def get_r(a, cx, cy):

    # i = np.indices(a.shape)
    # ix = (i[1, :, :] - cx) ** 2 # Nota: En numpy las imagenes no estan dadas de la forma (width, heigth) sino de la forma (rows, cols)
    # iy = (i[0, :, :] - cy) ** 2 # Nota: En numpy las imagenes no estan dadas de la forma (width, heigth) sino de la forma (rows, cols)
    # r = np.sqrt(ix + iy)

    ix = np.tile(np.array(range(1, a.shape[0]+1)).reshape(a.shape[0], 1), (1, a.shape[1]))
    iy = np.tile(np.array(range(1, a.shape[1]+1)).reshape(1, a.shape[1]), (a.shape[0], 1))

    ix = (ix - cx) ** 2
    iy = (iy - cy) ** 2

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

        # Nota: En numpy las imagenes no estan dadas de la forma (width, heigth) sino de la forma (rows, cols)
        # Por la tanto una imagen de 1280 x 960 pixeles tiene shape (960, 1280)
        a = np.ones((cube[key][2]['Height'], cube[key][2]['Width'])) 
        
        cx, cy = cube[key][2]['Vcenter']

        r = get_r(a, cx, cy)

        k = [float(k_) for k_ in (cube[key][2]['Vpoly'])]

        den = 1 + k[0]*r + k[1]*r**2 + k[2]*r**3 + k[3]*r**4 + k[4]*r**5 + k[5]*r**6

        V[key] = 1 / den

        # if '444' in key:
        #     print(f'{V}\n')

    return V

def get_Rv(cube):

    Rv = {'Blue-444'    : [], 'Blue'    : [], 
          'Green-531'   : [], 'Green'   : [], 
          'Red-650'     : [], 'Red'     : [], 
          'Red edge-705': [], 'NIR'     : [], 
          'Red edge-740': [], 'Red Edge': []
    }

    for key in cube.keys():

        _, a2, a3 = cube[key][2]['RadioCal']
        Te = cube[key][2]['Te']

        y = np.tile(np.array(range(1, cube[key][2]['Width']+1)).reshape(1, cube[key][2]['Width']), (cube[key][2]['Height'], 1))

        #den = np.array([1 + (a2*y/Te) - (a3*y) for y in range(cube[key][2]['Height'])])
        den = 1 + (a2*y/Te) - (a3*y)

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

def get_L(cube, V, Rv, Pc):

    L = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    for key in L.keys():

        g        = cube[key][2]['Gain']
        Te       = cube[key][2]['Te']
        a1, _, _ = cube[key][2]['RadioCal']
        norm     = cube[key][2]['Norm']

        a1 = float(a1)

        L[key] = V[key]*Rv[key]*Pc[key]

        L[key] = np.where(L[key]<0., 0., L[key])

        L[key] = (L[key]*a1) / (g*Te*norm)

    return L

def get_R(F, L):

    R = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    for key in F.keys():

        R[key] = L[key] * F[key]

        # cv2.imshow(f'R {key}', R[key])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    return R


#### Metodo 2 ###

def get_In(cube, ims):

    In = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    for key in In.keys():

        norm = cube[key][2]['Norm']
        bl = cube[key][2]['BL']

        ro_bl = bl / norm

        ro = ims[key] / norm

        In[key] = ro - ro_bl

    return In

def get_L2(cube, V, Rv, Pn):

    L2 = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    for key in L2.keys():

        a1, _, _ = cube[key][2]['RadioCal']
        g = cube[key][2]['Gain']
        Te = cube[key][2]['Te']
        # print(f'{a1}, {type(g)}, {float(a1)}, {type(Te)}')

        k = float(a1) / (g*Te)

        num = (V[key]*k*Pn[key]).T*Rv[key]

        # print(f'{num.shape=}, {np.min(num)=}, {np.max(num)=}, {num.dtype}\n')

        # if '444' in key:
        #     print(f'{num}')

    return L2







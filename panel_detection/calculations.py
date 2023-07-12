import numpy as np
from .process_img import get_panels
import tifffile

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
        a = np.ones((cube[key][1]['Height'], cube[key][1]['Width'])) 
        
        cx, cy = cube[key][1]['Vcenter']

        r = get_r(a, cx, cy)

        k = [float(k_) for k_ in (cube[key][1]['Vpoly'])]

        den = 1 + k[0]*r + k[1]*r**2 + k[2]*r**3 + k[3]*r**4 + k[4]*r**5 + k[5]*r**6

        V[key] = 1 / den

        # if '444' in key:
        #     print(f'{V[key]}\n')

    return V

def get_Rv(cube):

    Rv = {'Blue-444'    : [], 'Blue'    : [], 
          'Green-531'   : [], 'Green'   : [], 
          'Red-650'     : [], 'Red'     : [], 
          'Red edge-705': [], 'NIR'     : [], 
          'Red edge-740': [], 'Red Edge': []
    }

    for key in cube.keys():

        _, a2, a3 = cube[key][1]['RadioCal']
        Te = cube[key][1]['Te']

        y = np.tile(np.array(range(1, cube[key][1]['Width']+1)).reshape(1, cube[key][1]['Width']), (cube[key][1]['Height'], 1))

        #den = np.array([1 + (a2*y/Te) - (a3*y) for y in range(cube[key][1]['Height'])])
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

        bl = cube[key][1]['BL']

        I[key] = ims[key] - bl

        # if '444' in key:
        #     print(f'{I[key]}\n')

    return I

def get_L(metacube, imgcube):

    L = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    # Polinomio de vineta
    V = get_V(metacube)
    #print(V_lambda)

    Rv = get_Rv(metacube)
    #print(Rv_lambda)

    # Imagen original corregida a nivel de negro
    Pc = correct_im(metacube, imgcube)
    #print(Pc_lambda)

    for key in L.keys():

        g        = metacube[key][1]['Gain']
        Te       = metacube[key][1]['Te']
        a1, _, _ = metacube[key][1]['RadioCal']
        norm     = metacube[key][1]['Norm']

        a1 = float(a1)

        L[key] = V[key]*Rv[key]*Pc[key]

        L[key] = np.where(L[key]<0., 0., L[key])

        L[key] = (L[key]*a1) / (g*Te*norm)

        # if '444' in key:
        #     print(f'{a1=}, {Te=}, {g=}, {norm=}') 
        #     print(f'{L[key]}\n')

    return L

# Funcion para calcular el factor de calibracion F(lambda)
def get_F(cube, L):

    F = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    for key in cube.keys():

        ro = cube[key][0]
        
        I = get_panels(cube[key][2], L[key])

        F[key] = ro / I

    return F

def get_R(L, F, fn):

    R = {'Blue-444'    : [], 'Blue'    : [], 
         'Green-531'   : [], 'Green'   : [], 
         'Red-650'     : [], 'Red'     : [], 
         'Red edge-705': [], 'NIR'     : [], 
         'Red edge-740': [], 'Red Edge': []
    }

    arrays = []

    for key in F.keys():

        R[key] = L[key] * F[key]

        arrays.append(R[key])

        # cv2.imshow(f'R {key}', R[key])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    stack = np.stack(arrays)

    print(stack.shape)

    tifffile.imsave(fn, stack)

    return R








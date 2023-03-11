import math
#import numpy as np
def sumvec(a, b):
    c=[]
    if len(a) == len(b):
        for i in range(len(a)):
           c.append(a[i]+b[i])
    else:
        c ="Error. vectores con tamaño diferente"
    return c

def invec(v):
    resp = []
    for k in range(len(v)):
        resp.append(-1*v[k])
    return resp

def multescalar(k,v):
    resp = []
    for i in range(len(v)):
        resp.append(k * v[i])
    return resp

def summa(a,b):
    fil_a = len(a)
    fil_b = len(b)
    col_a = len(a[0])
    col_b = len(b[0])
    matriz = []
    if fil_a == fil_b and col_a == col_b:
        for i in range(fil_a):
            fila = []
            for j in range(col_a):
                fila.append(a[i][j]+b[i][j])
            matriz.append(fila)
    else:
        matriz = "Error, Tamaños diferentes"
    return matriz

def invma(a):
    fil_a = len(a)
    col_a = len(a[0])
    for i in range(fil_a):
        for j in range(col_a):
            a[i][j] = -1*(a[i][j])
    return a

def multescma(k,a):
    fila = len(a)
    col = len(a[0])
    for i in range(fila):
        for j in range(col):
            a[i][j] = k*a[i][j]
    return a

def traspo(a):
    fila = len(a)
    col = len(a[0])
    new = [[0 for m in range(fila)] for n in range(col)]
    for i in range(fila):
        for j in range(col):
            new[j][i]=a[i][j]
    return new

def conjugat(a):
    fil = len(a)
    col = len(a[0])
    for i in range(fil):
        for j in range(col):
            a[i][j] = a[i][j].conjugate()
    return a

def adjunta(a):
    a = traspo(a)
    a = conjugat(a)
    return a

def productoma(a,b):
    fil_a = len(a) #m
    col_a = len(a[0]) #n
    fil_b = len(b) #n
    col_b = len(b[0]) #p
    if col_a == fil_b:
        matriz = []
        for k in range(col_b):
            fila = []
            for i in range(fil_a):
                suma = 0
                for j in range(col_a):
                    suma += a[k][j]*b[j][i]
                fila.append(suma)
            matriz.append(fila)
    else: 
        matriz = "Error, Tamaños erroneos"
    return matriz

def accionmsobrev(a,v):
    fil_a = len(a) #m
    col_a = len(a[0]) #n
    fil_v = len(v) #n
    if col_a == fil_v:
        vector = []
        for i in range(fil_a):
            suma = 0
            for j in range(col_a):
                suma += a[i][j]*v[j]
            vector.append(suma)
    else: vector = "Error, verificar entrada"
    return vector

def producintern(v1,v2):
    if len(v1) == len(v2):
        suma = 0
        for i in range(len(v1)):
            suma += v1[i].conjugate()*v2[i]
    else: suma = "Error, tamaños erroneos"
    return suma

def normalvec(v):
    b = producintern(v,v)
    b = round(math.sqrt(b.real),2)
    return b

def distvec(u,v):
    h = sumvec(u,invec(v))
    dis = normalvec(h)
    return dis

def val_vec_propios(a):
    a = np.asarray(a)
    tam = a.shape
    fil = tam[0]
    col = tam[1]
    if fil == col:
        valores , vectores = np.linalg.eig(a)
        vectores = np.transpose(vectores)
        valor = np.round(valores,2)
        vector = np.round(vectores,2)
        return  "valores: {}. vectores: {}".format(valor,vectores[0])
    else:
        return "Error, matriz no cuadrada"

def unitario(a):
    if len(a) == len(a[0]):
            adjunt = adjunta(a)
            comprobador = productoma(a,adjunt)
            verificador = True
            for i in range(len(comprobador)):
                for j in range(len(comprobador)):
                    if (i == j and comprobador[i][j] != 1) or (i != j and comprobador[i][j] != 0):
                        verificador = False
                        break
            if verificador:
                resp = "La matriz es unitaria"
            else:
                resp = "La matriz NO es unitaria"
    else:
        resp = "Error, tamaño de matriz incorrecto"
    return resp

def hermitiana(a):
    if len(a) == len(a[0]):
            adjunt = adjunta(a)
            verificador = True
            for i in range(len(adjunt)):
                for j in range(len(adjunt)):
                    if a[i][j] != adjunt[i][j]:
                        verificador = False
                        break
            if verificador:
                resp = "La matriz es hermitiana"
            else:
                resp = "La matriz NO es hermitiana"
    else:
        resp = "Error, tamaño de matriz incorrecto"
    return resp

def tensor_product(a,b):
    m = len(a)
    n = len(b)
    m_1 = len(a[0])
    n_1 = len(b[0])
    fil = m*n
    col = m_1*n_1
    result = [[0 for j in range(col)] for k in range(fil)]
    for j in range(fil):
        for k in range(col):
            result[j][k] = (a[j//n][k//n_1])*(b[j%n][k%n_1])
    return result
    
if __name__ == "__main__":
    a = [3 + 2j, 4 + 3j, 8 - 5j, -4]
    b = [5j, -3 + 4j, 8, 7j]
    v = [3 + 2j, 4 + 3j, 8 - 5j]
    k = 4 - 7j
    A = [[3+14j,2j,-4+8j],[1j,9-10j,-6-7j],[11+2j,3-4j,9+5j]]
    B = [[7-26j,9+24j,7-13j],[12-15j,-29+30j,8-25j],[17-16j,4+9j,5+18j]]
    #matrix = np.array([[-1,-1j],[1j,1]])
    n = [[2,3],[1,4]]
    m = [[5,3,2],[1,0,2],[-2,5,6]]
    """print(sumvec(a,b))
    print(invec(a))
    print(multescalar(k,a))
    print(summa(A,B))
    print(invma(A))
    print(multescma(k,A))
    print(traspo([[6+2j, 4-1j], [-2j, 6-14j], [7-8j, 3j]]))
    print(conjugat(A))
    print(adjunta(B))
    print(productoma(A,B))
    print(accionmsobrev(A,v))
    print(producintern([3+4j,8,0,1+3j],[1j,5-4j,7j,3j]))
    print(normalvec([1+2j,3-4j,-3j]))
    print(distvec([4,2-1j,2+4j],[4-3j,-1j,2j]))
    print(val_vec_propios([[-1,-1j],[1j,1]]))
    print(unitario([[2/3,(-2+1j)/3],[(2+1j)/3,2/3]]))
    print(hermitiana([[3,2-1j,-5j],[2+1j,0,9-5j],[5j,9+5j,6]]))"""
    print(tensor_product(n,m))
    print(hermitiana([[2j,0], [0,-2j]]))


#Sebastian Cardona Parra
#CNYT 2023-1

import numpy as np
import matplotlib.pyplot as plot
import libvecspaces as lvs
import math

def modulo_cuadrado(c):
    return round(c.real**2+c.imag**2,2)

def calculo(matrix,vecto,clics):
    if clics == 0:
        return vecto
    elif clics == 1:
        return lvs.accionmsobrev(matrix,vecto)
    else:
        return lvs.accionmsobrev(matrix,calculo(matrix,vecto,clics-1))

#reto 3.1.1 sistema detriministico
def canicas(matrix,vecto,clics):
    if len(matrix) != len(matrix[0]):
        result = "Error, tamaño incorrecto de matriz"
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0 or matrix[i][j] != 1:
                result = "Matriz no booleana"
                break
    else:
        result = calculo(matrix,vecto,clics)
    return result
#reto 3.2.1 sistema probabilistico
def fracciones(matrix,vecto,clics):
    if len(matrix) != len(matrix[0]):
        result = "Error, tamaño incorrecto de matriz"
    for i in range(len(matrix)):
        suma = 0
        for j in range(len(matrix[0])):
            suma += matrix[i][j]
        if suma != 1:
            result = "Error, matriz no doblemente estocástica"
            break
    for i in range(len(lvs.traspo(matrix))):
        suma = 0
        for j in range(len(lvs.traspo(matrix)[0])):
            suma += matrix[i][j]
        if suma != 1:
            result = "Error, matriz no doblemente estocástica"
            break
    else:
        result = calculo(matrix,vecto,clics)
        result = [round(x,2) for x in result]
    return result

#reto 3.2.2 probabilisto mas de dos rendija
def experimento_rendijas(blancos,rendijas):

    matriz = [[0 for x in range(blancos+rendijas+1)] for x in range(blancos+rendijas+1)]
    cada = blancos//rendijas if blancos%2==0 else (blancos+1)//(rendijas)

    j=rendijas+1

    for k in range(1,rendijas+1):
        matriz[k][0]=round(1/rendijas,2)
        for i in range(j,j+cada):
            matriz[i][k]= round(1/cada,2)
        j+=cada-1

        for l in range(len(matriz)-blancos,len(matriz)):
            matriz[l][l]=1
    vector = [0 for x in range(len(matriz))]
    vector[0] = 1
    matriz1 = lvs.productoma(matriz,matriz)
    vector = lvs.accionmsobrev(matriz1,vector)

    return matriz,vector

#reto 3.3.1 sistema probabilistico cuántico

def complejos(matrix,vecto,clics):
    if len(matrix) != len(matrix[0]):
        result = "Error, tamaño incorrecto de matriz"
    for i in range(len(matrix)):
        suma = 0
        for j in range(len(matrix[0])):
            suma += modulo_cuadrado(matrix[i][j])
        if suma != 1:
            result = "Error, matriz no doblemente estocástica"
            break
    for i in range(len(lvs.traspo(matrix))):
        suma = 0
        for j in range(len(lvs.traspo(matrix)[0])):
            suma += modulo_cuadrado(matrix[i][j])
        if suma != 1:
            result = "Error, matriz no doblemente estocástica"
            break
    else:
        result = calculo(matrix,vecto,clics)
    return result

#reto 3.3.2 cuántico más de dos rendijas
def experimento_rendijas_cua(matriz):
    
    vector = [0 for x in range(len(matriz))]
    vector[0] = 1
    matriz = lvs.productoma(matriz,matriz)
    vector = lvs.accionmsobrev(matriz,vector)

    return vector

def graficar(vector):
    data =len(vector)
    x = np.array([x for x in range(data)])
    y = np.array([round(vector[x] * 100, 2) for x in range(data)])

    plot.bar(x, y, color='b', align='center')
    plot.title('Probabilidad del vector en unidades de %')
    plot.savefig("Caso.jpg")
    plot.show()
    
if __name__ == "__main__":
    print(canicas([[0,0,1],[1,0,0],[0,1,0]],[3,6,9],5))
    print(fracciones([[1/3,2/3,0],[2/3,1/3,0],[0,0,1]],[1,0,0],3))
    print(experimento_rendijas(5,2))
    print(complejos([[1/math.sqrt(2),1/math.sqrt(2),0],[-1j/math.sqrt(2),1j/math.sqrt(2),0],[0,0,1j]],[1/math.sqrt(3),2j/math.sqrt(15),math.sqrt(2/5)],1))
    print(graficar(fracciones([[1/3,2/3,0],[2/3,1/3,0],[0,0,1]],[1,0,0],1)))

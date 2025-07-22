# Definir una matriz 3x3 con valores numericos

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def buscar_valor(matriz,valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==valor:
                return i,j
    return None

numero_buscar=9

resultado = buscar_valor(matriz,numero_buscar)

if resultado:
    print(f"el resultado del numero {numero_buscar} se encuentra en la posicion (fila: {resultado[0]}, columna: {resultado[1]}).")

else:
    print(f"el numero no se encontro en la matriz")
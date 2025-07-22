# Ordenar matriz

matriz = [
    [11, 6, 15],
    [9, 2, 14],
    [8, 20, 7]
]

def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


print("Matriz Original:")
mostrar_matriz(matriz)


for fila in matriz:
    bubble_sort_fila(fila)


print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)


# Creamos el archivo "my_notes.txt"
# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r')

file = open("my_notes.txt", "r")

# Leemos y mostramos cada línea del archivo una por una

print("Contenido del archivo:")
linea = file.readline()  # Leemos la primera línea

while linea:  # Mientras haya contenido

    print(linea.strip())  # Mostramos la línea sin saltos de línea adicionales
    linea = file.readline()  # Leemos la siguiente línea



# Cerramos el archivo manualmente
file.close()
# 1. Crea un diccionario llamado informacion personal

informacion_personal={
    "nombre":"Carlos",
    "edad":33,
    "ciudad":"Guayaquil",
    "profesion":"Contador",
    "hobbi":"correr"
}

print(informacion_personal)

# 2. Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.

informacion_personal["ciudad"]="Cuenca"

# 3. Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"]= "0968963999"

# 4. Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.

del informacion_personal["edad"]

# Imprime el diccionario resultante después de realizar todas las operaciones.

print(informacion_personal)

# Creación y escritura en el archivo my_notes.txt
# Abrimos el archivo en modo escritura ("w") para crear y escribir en él.
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Primera línea de mis notas personales.\n")
    file.write("Segunda línea con más información relevante.\n")
    file.write("Tercera línea para finalizar mis notas.\n")

# Lectura del archivo my_notes.txt
# Abrimos el archivo en modo lectura ("r") para leer su contenido.
with open("my_notes.txt", "r") as file:
    # Usamos un bucle para leer línea por línea con el método readline().
    line = file.readline()
    while line:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # strip() quita los saltos de línea al final
        # Leemos la siguiente línea
        line = file.readline()

# Al finalizar, el archivo se cierra automáticamente gracias a la estructura 'with'.

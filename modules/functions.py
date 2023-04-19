FILEPATH = "notas.txt"

def ObtenerNotas(filePath = FILEPATH):
    """Lee el archivo y devuelve una lista con el texto"""
    with open(filePath, 'r') as file:
        notas = file.readlines() 
    return notas

def EscribirNotas(notas,  filePath = FILEPATH):
    """Escribe la lista en el archivo de texto"""
    with open(filePath, 'w') as file:
        notas = file.writelines(notas)
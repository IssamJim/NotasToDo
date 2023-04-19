from modules import functions
import time

fecha = time.strftime("%b %d, %Y %H:%M:%S")
print("La fecha de hoy es", fecha)

while True:   
    opciones = input("Escribe Agregar, Mostrar, Editar, Completar o Salir: ")
    opciones = opciones.strip() #Quita espacios al inicio y al final.


    #Opcion Agregar nota
    if opciones.startswith("Agregar"):
        nota = opciones[8:]

    #Guardamos lo que hay en el archivo en la variable notas
        notas = functions.ObtenerNotas()

    #Agregamos la nueva nota
        notas.append(nota + '\n')

    #Guardamos la nueva lista de notas en el archivo
        functions.EscribirNotas(notas) 


    #Opcion Mostrar
    elif opciones.startswith("Mostrar"):

    #Guardamos las notas en una variable
        notas = functions.ObtenerNotas()

    #enumerate para numerar las notas, le quitamos salto de linea extra y aumentamos index en 1 por empezar en 0
        for index, item in enumerate(notas):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print (row)


    #Opcion Editar
    elif opciones.startswith("Editar"):
        try:
            numero = int(opciones[6:])
            print(numero)

            numero = numero - 1

            notas = functions.ObtenerNotas()

            nuevaNota = input("Escriba la nueva nota: ")
            notas[numero] = nuevaNota + '\n' 

            functions.EscribirNotas(notas)
        except ValueError:
            print("Comando no valido.")
            continue
        
        #Completar
    elif opciones.startswith("Completar"):
        try:
            numero = int(opciones[10:])

            notas = functions.ObtenerNotas()

            index = numero - 1
            NotaCompletada = notas[index].strip('\n')
            notas.pop(index)

            functions.EscribirNotas(notas)

            message = f"Nota {NotaCompletada} se completo."
            print(message)
        except IndexError:
            print("No hay nota con ese numero.")
            continue

    elif opciones.startswith('Salir'):
        break
    else:
        print("Comando no valido")

print("Bye")


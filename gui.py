from modules import functions
import PySimpleGUI as sg

label = sg.Text("Escribe una nota")
inputBox = sg.InputText(tooltip="Escriba la nota", key="nota")
addButton = sg.Button("Agregar")

window = sg.Window("App de Notas",
                    layout=[[label], [inputBox, addButton]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Agregar":
            notas = functions.ObtenerNotas()
            nuevaNota = values['nota'] + "\n"
            notas.append(nuevaNota)
            functions.EscribirNotas(notas)
    elif sg.WIN_CLOSED:
          break

window.close()

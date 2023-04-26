from modules import functions
import PySimpleGUI as sg

label = sg.Text("Escribe una nota")
inputBox = sg.InputText(tooltip="Escriba la nota", key="nota")
addButton = sg.Button("Agregar")
listBox = sg.Listbox(values = functions.ObtenerNotas(), key = 'notas',
                       enable_events=True, size=[45, 10])
editButton = sg.Button("Editar")

window = sg.Window("App de Notas",
                    layout=[[label], [inputBox, addButton],[listBox, editButton]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Agregar":
            notas = functions.ObtenerNotas()
            nuevaNota = values['nota'] + "\n"
            notas.append(nuevaNota)
            functions.EscribirNotas(notas)
            window['notas'].update(values=notas)
        case "Editar":
            notaEditar = values['notas'][0]
            nuevaNota = values['nota']

            notas = functions.ObtenerNotas()
            index = notas.index(notaEditar)
            notas[index] = nuevaNota
            functions.EscribirNotas(notas)
            window['notas'].update(values=notas)
        case 'notas':
            window['nota'].update(value=values['notas'][0])
        case sg.WIN_CLOSED:
            break

window.close()

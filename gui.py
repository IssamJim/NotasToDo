from modules import functions
import PySimpleGUI as sg
import time

sg.theme("BluePurple")

reloj = sg.Text('', key='reloj')
label = sg.Text("Escribe una nota")
inputBox = sg.InputText(tooltip="Escriba la nota", key="nota")
addButton = sg.Button("Agregar")
listBox = sg.Listbox(values = functions.ObtenerNotas(), key = 'notas',
                       enable_events=True, size=[45, 10])
editButton = sg.Button("Editar")
completeButton = sg.Button("Completar")
salirBoton = sg.Button("Salir")

window = sg.Window("App de Notas",
                    layout=[[reloj],
                            [label],
                            [inputBox, addButton],
                            [listBox, editButton, completeButton],
                            [salirBoton]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["reloj"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
            try:
                notaEditar = values['notas'][0]
                nuevaNota = values['nota']

                notas = functions.ObtenerNotas()
                index = notas.index(notaEditar)
                notas[index] = nuevaNota
                functions.EscribirNotas(notas)
                window['notas'].update(values=notas)
            except IndexError:
                sg.popup("Seleccione un tarea a editar", font=("Helvetica", 20) )
        case 'notas':
            window['nota'].update(value=values['notas'][0])
        case 'Completar':
            try:
                notaCompleta = values['notas'][0]
                notas = functions.ObtenerNotas()
                notas.remove(notaCompleta)
                functions.EscribirNotas(notas)
                window['notas'].update(values=notas)
                window['nota'].update(value='')
            except IndexError:
                sg.popup("Seleccion una tarea a completar.", font=("Helvetica", 20))
        case 'Salir':
            break
        case sg.WIN_CLOSED:
            break

window.close()

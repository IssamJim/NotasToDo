from modules import functions
import PySimpleGUI as sg

label = sg.Text("Escribe una nota")
inputBox = sg.InputText(tooltip="Escriba la nota")
addButton = sg.Button("Agregar")

window = sg.Window("App de Notas", layout=[[label], [inputBox, addButton]])
window.read()
window.close()

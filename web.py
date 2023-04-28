import streamlit as st 
from modules import functions

notas = functions.ObtenerNotas()

def agregarNota():
    nota = st.session_state["nuevaNota"] + "\n"
    notas.append(nota)
    functions.EscribirNotas(notas)


st.title("Notas")
st.subheader("WebApp de notas")
st.write("Para incrementar la productividad")

for index, nota in enumerate(notas):
    checkbox = st.checkbox(nota, key=nota)
    if checkbox:
        notas.pop(index)
        functions.EscribirNotas(notas)
        del st.session_state[nota]
        st.experimental_rerun()

st.text_input(label="", placeholder="Agrega una nota...",
              on_change=agregarNota, key="nuevaNota")

print ("Hello")
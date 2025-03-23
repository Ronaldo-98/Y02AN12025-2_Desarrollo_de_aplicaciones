import streamlit as st

#Titulo de la aplicación
st.title("Bienvenido a mi aplicación")

#Solicitar el nombre del usuario
nombre = st.text_input("por favor, ingresa tu nombre ")

#Mostrar el saludo si el usuario ingresa su nombre
if nombre:
    st.write(f"Hola, {nombre} ! Bienvenido a esta aplicación web de Streamlit")
    
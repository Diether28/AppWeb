import streamlit as st

home = st.Page(
    page="view/home.py",
    title="Inicio",
    icon="🏠",
    default=True
)

acerca_de = st.Page(
    page="view/acerca_de.py",
    title="Acerca de",
    icon="👤",
)

project_1 = st.Page(
    page="view/ventas.py",
    title="Ventas",
    icon="🛒"
)

project_2 = st.Page(
    page="view/chatbot.py",
    title="Chatbot"
    icon="🤖"
)
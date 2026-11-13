import streamlit as st

st.title("Uma mensagem especial ❤️")

nome = st.text_input("Qual é o seu nome?").strip().lower()

if nome:
    if nome in ["pamela", "pamela patricia", "pamela matos", "pamelinha", "paty"]:
        st.success("Só queria te dizer que você é muito especial! ❤️")
        st.write("Tenha um ótimo dia! Te amo gostosa.")
    else:
        st.write("Esse código não é pra você. 😊")

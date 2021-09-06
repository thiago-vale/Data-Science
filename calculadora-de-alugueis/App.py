# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 13:37:54 2021

@author: Thiago
"""

import streamlit as st
from catboost import CatBoostRegressor

@st.cache
def load_model(model_path = "./Modelo/model_catr.cbm"):
    model = CatBoostRegressor()
    model.load_model(model_path)
    return model

model = load_model("./Modelo/model_catr.cbm")

st.title("Calculadora de Alugueis")
st.subheader("Entre com as caracteristicas do seu imovel")

bairro = st.selectbox("Nome do Bairro", options= ["botafogo","copacabana","ipanema ","cosme_velho",
                                                  "leblon","flamengo","laranjeiras","lagoa","catete",
                                                  "leme","glória","humaitá", "gávea", "jardim_botanico",
                                                  "são_conrado", "urca"])

area = st.number_input(label='Área do apartamento', min_value=10, max_value=1000,value=50)

condominio = st.number_input(label='Valor do condominio', min_value=50, max_value=10000,value=500, step=50)


quartos = st.slider(label="# quartos", min_value=0, max_value=5, value=2)
banheiros = st.slider(label="# banheiros", min_value=0, max_value=5, value=2)
garagens = st.slider(label="# garagens", min_value=0, max_value=5, value=2)

preco = model.predict([area, condominio, quartos, banheiros, garagens, bairro])

if st.button(label="Calcular"):
    st.subheader(f"Preço estimado: R$ {preco:,.2f}")
    with open("memoria.csv", "a") as f:
        f.writelines(
            f"{bairro},{area},{condominio},{quartos},{banheiros},{garagens},{preco}\n")
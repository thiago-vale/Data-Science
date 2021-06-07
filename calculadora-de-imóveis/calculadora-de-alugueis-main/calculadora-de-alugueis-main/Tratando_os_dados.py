# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 07:54:06 2021

@author: Thiago
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/Thiago/Desktop/Potifolio/Projeto calculadora de imoveis/Data Sets/todos_os_resultados.csv')

df = df.drop_duplicates(keep="first", subset=[coluna for coluna in df.columns if coluna!="crawled_at"]).reset_index(drop=True)
filtro_de_anuncios = [str(_id).isnumeric() for _id in df["id"]]
df = df[filtro_de_anuncios].reset_index(drop=True)
df["rooms"].str.split(" ").str[0].str.replace("--" , "0")
df["Quarto"] = (df["rooms"].str.split(" ").str[0].str.replace("--","0").astype(int))
df["Banheiro"] = (df["bathrooms"].str.split(" ").str[0].str.replace("--","0").astype(int))
df["Garagem"] = (df["garages"].str.split(" ").str[0].str.replace("--","0").astype(int))
df["condo"] = df["condo"].fillna("MISSING")
df["condominio"] = [int(w.split("R$ ")[1].replace(".","")) if w!="MISSING" else np.nan for w in df["condo"]]
df["preço"] = [int(w.split("R$ ")[1].split(" /")[0].replace(".","")) for w in df["price"]]
df["area_limpo"] = df["area"].astype(int)
df["crawled_at"] = pd.to_datetime(df["crawled_at"], format="%Y-%m-%d %H:%M")
df = df.drop(columns = ["area", "rooms", "bathrooms", "garages", "price", "condo"])
df["bairro"] = (df["address"].str.split("- ").str[1].str.split(",").str[0])
df.loc[df["bairro"].isin(["RJ"]), "bairro"] = (df.loc[df["bairro"].isin(["RJ"]), "address"].str.split(",").str[0])
df.loc[df["crawler"]!=df["bairro"],"bairro"].unique()
df["crawler"] = (df["crawler"].str.lower().str.replace(" ","_"))
df["bairro"] = (df["bairro"].str.lower().str.replace(" ","_").str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8"))
df = df.drop(columns="bairro")
df["amenities"] = df["amenities"].str.split("\n")
df["amenities"] = df["amenities"].fillna("")
amenities = []
for am in df["amenities"]:
    if am != "":
        amenities = amenities + am
unico_amenities = list(set(amenities))
df["amenities"] = df["amenities"].str.join(", ")
for amenity in unico_amenities:
    print(amenity)
    df[amenity]=0
    df.loc[df["amenities"].str.contains(amenity), amenity] = 1
df.to_csv("C:/Users/Thiago/Desktop/Potifolio/Projeto calculadora de imoveis/Data Sets/aptos_csv2.csv", index=False)
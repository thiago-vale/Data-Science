# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:37:08 2021

@author: Thiago
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv("C:/Users/Thiago/Desktop/Potifolio/Projeto calculadora de imoveis/Data Sets/aptos_csv.csv")
order = df[["crawler", "preço"]].groupby("crawler").mean().sort_values(by="preço").index

def iqr(df):
    q1,q3 = df.quantile([.25 , .75])
    iqr= q3-q1
    lower_bound= q1 - 1.5*iqr
    upper_bound= q3 + 1.5*iqr
    pct_outliers = sum(~df.between(lower_bound, upper_bound))/len(df)
    return lower_bound , upper_bound, round(pct_outliers,2)

def percentiles(df, percentiles_levels=0.1):
    lower_bound, upper_bound = df.quantile([percentiles_levels, 1-percentiles_levels])
    pct_outliers = sum(~df.between(lower_bound, upper_bound))/len(df)
    return lower_bound, upper_bound, round(pct_outliers,2)

coluna = "preço"
for bairro in df["crawler"].unique():
    metodo = "iqr"
    lower_bound, upper_bound, pct_outliers = iqr(df.loc[df["crawler"]==bairro, coluna])
    if pct_outliers>0.35:
        metodo = "percentile"
        lower_bound, upper_bound, pct_outliers = percentiles(df.loc[df["crawler"]==bairro, coluna])
        print(f"Coluna: {coluna}, bairro: {bairro}, metodo: {metodo}, pct_outliers: {pct_outliers}")
        df.loc[(df["crawler"]==bairro) & 
           (~df[coluna].between(lower_bound, upper_bound)), coluna]=np.nan
        
df.loc[df["preço"]>130000, "preço"]=np.nan

def plot_stripplot(df, var_name):
    order = df[["crawler", var_name]].groupby("crawler").mean().sort_values(by=var_name).index
    plt.figure(figsize=(10,10))
    return sns.stripplot(data=df, 
                         x=var_name, y="crawler", 
                         order=order)

coluna = "condominio"
for bairro in df["crawler"].unique():
    metodo = "iqr"
    lower_bound, upper_bound, pct_outliers = iqr(df.loc[df["crawler"]==bairro, coluna])
    if pct_outliers>0.35:
        metodo = "percentile"
        lower_bound, upper_bound, pct_outliers = percentiles(df.loc[df["crawler"]==bairro, coluna])
        print(f"Coluna: {coluna}, bairro: {bairro}, metodo: {metodo}, pct_outliers: {pct_outliers}")
        df.loc[(df["crawler"]==bairro) & 
           (~df[coluna].between(lower_bound, upper_bound)), coluna]=np.nan
        
df = df.dropna(subset=["area_limpo","Banheiro", "Quarto","condominio", "Garagem", "preço"])

df = df.reset_index(drop=True)

df.to_csv("C:/Users/Thiago/Desktop/Potifolio/Projeto calculadora de imoveis/Data Sets/Aptos_sem_outliers.csv", index=False)
        
        
        
        
        
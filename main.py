#Bibliotecas necessárias

import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

#Função de carregamento de dados(Extract -> Yahoo Finance)
@st.cache_data
def load_data(empresas):
    tickers_text = " ".join(empresas)
    stock_data = yf.Tickers(tickers_text)
    stock_quotes = stock_data.history(start="2010-01-01", end="2025-03-05")
    stock_quotes = stock_quotes["Close"]
    return stock_quotes 

#Definição das ações desejadas e carregamento dos dados em si 
stocks = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA", "VALE3.SA", "ABEV3.SA", "GGBR4.SA"]
loaded_data = load_data(stocks) 

#Título de Início da aplicação
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações de mercado ao longo dos anos (2010-2024)
""") # markdown

#Preparação dos filtros/Visualizações

#Criação da Sidebar
st.sidebar.header("Filtros")

#Filtro de Ações/Stocks
stock_list = st.sidebar.multiselect("Escolha uma ação!", loaded_data.columns)
if stock_list:
    loaded_data = loaded_data[stock_list]
    if len(stock_list) == 1:
        unique_stock = stock_list[0]
        loaded_data = loaded_data.rename(columns = {unique_stock: "Close"})

#Filtro de Datas
initial_date = loaded_data.index.min().to_pydatetime()
final_date = loaded_data.index.max().to_pydatetime()

date_interval = st.sidebar.slider("Selecione o período", 
                  min_value=initial_date, 
                  max_value=final_date, 
                  value=(initial_date, final_date),
                  step=timedelta(days=15))

loaded_data = loaded_data.loc[date_interval[0]:date_interval[1]]

#Gráfico de linha das views entra aqui
st.line_chart(loaded_data)

#st.write("""
# Fim do App 
#""") # markdown
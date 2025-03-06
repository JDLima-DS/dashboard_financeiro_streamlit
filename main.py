import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def load_data(empresas):
    tickers_text = " ".join(empresas)
    stock_data = yf.Tickers(tickers_text)
    stock_quotes = stock_data.history(start="2010-01-01", end="2025-03-05")
    stock_quotes = stock_quotes["Close"]
    return stock_quotes 

stocks = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA", "VALE3.SA", "ABEV3.SA", "GGBR4.SA"]
loaded_data = load_data(stocks) 

st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações de mercado ao longo dos anos (2010-2024)
""") # markdown

#Preparação dos filtros/Visualizações

#gráfico das views entra aqui

stock_list = st.multiselect("Escolha uma ação!", loaded_data.columns)
if stock_list:
    loaded_data = loaded_data[stock_list]
    if len(stock_list) == 1:
        unique_stock = stock_list[0]
        loaded_data = loaded_data.rename(columns = {unique_stock: "Close"})

st.line_chart(loaded_data)

#st.write("""
# Fim do App 
#""") # markdown
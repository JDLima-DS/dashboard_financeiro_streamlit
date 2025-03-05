import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def load_data(empresa):
    stock_data = yf.Ticker(empresa)
    stock_quotes = stock_data.history(period='1d', start="2010-01-01", end="2025-03-05")
    stock_quotes = stock_quotes[["Close"]]
    return stock_quotes

loaded_data = load_data("ITUB4.SA") # Necessita-se do .SA, devido ser uma ação brasileira(São Paulo)

st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações do ITAÚ (ITUB4) ao longo dos anos (2010-2024)
""") # markdown

#gráfico das views entra aqui
st.line_chart(loaded_data)

st.write("""
# Fim do App 
""") # markdown
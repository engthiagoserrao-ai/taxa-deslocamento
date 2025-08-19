
import streamlit as st

st.set_page_config(page_title="Calculadora de Taxa de Deslocamento", page_icon="🚚")

st.title("Calculadora de Taxa de Deslocamento 🚚")

st.write("Informe a distância em quilômetros para calcular o valor da taxa de deslocamento (ida e volta).")
st.write("Valor considerado: **R$2,00 por km** (ida e volta = R$4,00 por km).")

# Entrada da distância
distancia_km = st.number_input("Distância (em km)", min_value=0.0, step=0.1)

# Botão para calcular
if st.button("Calcular Taxa"):
    taxa_total = distancia_km * 4  # ida e volta com R$2,00 por km
    st.success(f"💰 Valor total da taxa de deslocamento: R${taxa_total:,.2f}")

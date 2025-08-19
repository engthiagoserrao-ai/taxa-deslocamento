import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Ponto fixo em Chapecó
ponto_fixo = (-27.082740, -52.634639)

def endereco_para_coordenadas(endereco):
    geolocator = Nominatim(user_agent="taxa_deslocamento_app")
    local = geolocator.geocode(endereco)
    if local:
        return local.latitude, local.longitude
    return None, None

def calcular_distancia_km(lat, lng):
    destino = (lat, lng)
    return geodesic(ponto_fixo, destino).km * 2  # ida e volta

def calcular_taxa(distancia_km):
    return round(distancia_km * 2.00, 2)

# Interface Streamlit
st.title("Calculadora de Taxa de Deslocamento")
endereco = st.text_input("Digite o endereço completo:")

if endereco:
    lat, lng = endereco_para_coordenadas(endereco)
    if lat and lng:
        distancia = calcular_distancia_km(lat, lng)
        taxa = calcular_taxa(distancia)
        st.success(f"Distância total (ida e volta): {distancia:.2f} km")
        st.info(f"Taxa de deslocamento: R${taxa:.2f}")
    else:
        st.error("Endereço não encontrado.")

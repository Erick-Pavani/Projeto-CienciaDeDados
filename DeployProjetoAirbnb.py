# Imports
import pandas as pd
import streamlit as st
import joblib

# Separa as colunas com valores numéricos
x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

# Separa as colunas com valores de apenas 'True' ou 'False' (booleans)
x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

# Separa as colunas com valores de texto com várias opções
x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancelation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }

dicionario = {}
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0

# Ajustando os valores default de cada campo e as devidas formatações para cada um dos tipos de campo
for item in x_numericos:
    if item == "latitude" or item == "longitude":
        valor = st.number_input(
            f'{item}', step=0.00001, value=0.0, format='%.5f')
    elif item == "extra_people":
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    x_numericos[item] = valor

for item in x_tf:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == 'Sim':
        x_tf[item] = 1
    else:
        x_tf[item] = 1

for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[item])
    dicionario[f'{item}_{valor}'] = 1

botao = st.button('Prever valor do imóvel a ser anunciado!')

if botao:
    # Juntando os dicionários para criar um único dataframe
    dicionario.update(x_numericos)
    dicionario.update(x_tf)

    # Criando o dataframe
    valores_x = pd.DataFrame(dicionario, index=[0])

    # Lê o arquivo '.joblib' com o modelo pronto
    modelo = joblib.load('modelo.joblib')

    # Usa o modelo para fazer a previsão com base nos dados inseridos
    preco = modelo.predict(valores_x)

    # Printa o valor da previsão na página
    st.write(preco[0])

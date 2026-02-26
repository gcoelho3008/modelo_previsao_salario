import streamlit as st
import json
import requests

# Título da aplicação
st.title('Previsão de Salário')

# Formulário para entrada de dados
st.write('Preencha em meses o tempo de empresa')
tempo_na_empresa = st.slider('Tempo na Empresa (meses)', min_value=1, max_value=240, value=60, step=1)

st.write('Preencha o nível na empresa')
nivel_na_empresa = st.slider('Nível na Empresa (1 a 10)', min_value=1, max_value=10, value=5, step=1)

# Preparar os dados para api
input_features = {'tempo_na_empresa': tempo_na_empresa,
                  'nivel_na_empresa': nivel_na_empresa}

# Botão para fazer a previsão
if st.button('Prever Salário'):
    res = requests.post(url='http://127.0.0.1:8000/predict', data=json.dumps(input_features))
    res_json = json.loads(res.text)
    salario_em_reais = round(res_json['salario_em_reais'], 2)
    st.subheader(f'Previsão de Salário: R$ {salario_em_reais}')
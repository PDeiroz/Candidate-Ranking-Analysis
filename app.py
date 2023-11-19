import pandas as pd

# Carregar as planilhas
planilha_objetiva = pd.read_excel('C:/Users/paulo/Desktop/anailise de dados - concurso professor/planilha_objetiva.xlsx')
planilha_discursiva = pd.read_excel('C:/Users/paulo/Desktop/anailise de dados - concurso professor/planilha_discursiva.xlsx')

# Mesclar as planilhas pela coluna 'Nome'
planilha_final = pd.merge(planilha_discursiva, planilha_objetiva, on='Nome', suffixes=('_discursiva', '_objetiva'))

# codificação na coluna 'Número de Inscrição_x_discursiva'
if 'Número de Inscrição_x_discursiva' in planilha_final.columns:
    planilha_final['Número de Inscrição_x_discursiva'] = planilha_final['Número de Inscrição_x_discursiva'].astype(str).str.encode('latin1').str.decode('utf-8')

# Selecionar as colunas desejadas
colunas_selecionadas = ['Nome', 'Número de Inscrição_x_discursiva', 'Nota Discursiva', 'Número de Inscrição_x_objetiva', 'Nota Objetiva']
planilha_final = planilha_final[colunas_selecionadas]

# Renomear as colunas
planilha_final.columns = ['Nome', 'Número de Inscrição Discursiva', 'Nota Discursiva', 'Número de Inscrição Objetiva', 'Nota Objetiva']

# Salvar a planilha final em um novo arquivo Excel
planilha_final.to_excel('C:/Users/paulo/Desktop/anailise de dados - concurso professor/planilha_final.xlsx', index=False)


# Candidate-Ranking-Analysis
Análise de Dados - Concurso Professor

Este projeto consiste em duas partes principais: a primeira parte envolve a fusão de duas planilhas de dados de candidatos 
de um concurso para professores, e a segunda parte envolve a criação de um ranking com base nas notas dos candidatos.

# Tecnologias e Bibliotecas Utilizadas
Python
Pandas

# Instalação e Execução
Para instalar e executar este projeto, siga estas etapas:

Clone o repositório para sua máquina local.
Instale a biblioteca pandas com o comando pip install pandas.
Execute o script Python com o comando python script.py.

# Descrição do Projeto
Parte 1: Fusão de Planilhas
A primeira parte do projeto envolve a fusão de duas planilhas Excel. A primeira planilha contém os nomes dos candidatos, 
o número da inscrição e a nota da prova objetiva. A segunda planilha contém os nomes dos candidatos e a nota da prova discursiva.

O script Python carrega ambas as planilhas e as mescla pela coluna ‘Nome’. Em seguida, seleciona as colunas desejadas 
e as renomeia para maior clareza. Finalmente, salva a planilha final em um novo arquivo Excel.

Parte 2: Criação de Ranking
A segunda parte do projeto envolve a criação de um ranking com base nas notas dos candidatos. O script Python carrega as planilhas mescladas e calcula a pontuação total para cada candidato, que é a soma das notas discursivas e objetivas.

Em seguida, cria uma coluna de ranking com base na nota final, com o candidato de maior pontuação classificado em primeiro lugar. Finalmente, ordena o DataFrame pelo ranking e salva a planilha final em um novo arquivo Excel.

# Contribuições

Contribuições para este projeto são bem-vindas. Se você tiver alguma sugestão ou melhoria, sinta-se à vontade para fazer um fork do repositório e enviar um pull request.

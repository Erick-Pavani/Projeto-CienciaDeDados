# Projeto de ciência de dados
## Projeto realizado pelo curso Pyhton Impressionador

O projeto consiste em criar um modelo de previsão que consiga prever os preços de imóveis anunciados no AirBnb na cidade do Rio de Janeiro.
O foco do projeto são imóveis comuns de pessoas comuns, não casas imensas/mansões e não imóveis anunciados por imobiliárias etc, a idéia do projeto é que qualquer um possa usar esse modelo para precificar corretamente seu imóvel se eventualmente algum dia queira anunciá-lo pela primeira vez no AirBnb.

- Essa é uma solução completa incluindo todos os passos desde importar as bases até o deploy do modelo para o usuário final.

- As bases de dados usadas podem ser obtidas através de um link no arquivo do modelo. Os arquivos são grandes demais para estarem nesse repo.
 
# Como usar:
Passo 1:
- Abrir o link das bases de dados encontrado no arquivo "ModeloPrevisãoAirbnb.ipynb" e baixar as mesmas, coloque a pasta "dataset" na mesma pasta do código.

- Passo 2:
Executar o arquivo "ModeloPrevisãoAirbnb.ipynb" (recomendado executar via jupyter notebook, ou pela extensão do jupyter para vscode), ao fim da execução será criado na mesma pasta um arquivo chamado "modelo.joblib", contendo o modelo de machine laerning pronto.

- Passo 3:
Execute o arquivo "DeployProjetoAirbnb.py" através do anaconda prompt(navegue até a pasta onde os arquivos se encontram) usando o comando "streamlit run DeployProjetoAirbnb.py"

- Passo 4:
Uma janela do navegador se abrirá (caso não abra automaticamente, copie o link escrito em azul no anaconda prompt e cole no navegador desejado)

- Passo 5:
Preencha as informações com as informações do imóvel desejado e use o modelo de previsão para ter resultados mais precisos e consistentes no preço dos seus imóveis que serão anunciados no airbnb no RJ.
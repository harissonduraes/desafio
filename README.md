## Webscraping e análise de dados com python

Este é um desafio da Seazone que tive a oportunidade de fazer, agradeço desde já.
Os códigos fazem webscraping e análise dos dados adquiridos usando python.
O site é o de anúncios da Olx. A página dos terrenos é: https://sc.olx.com.br/florianopolis-e-regiao/imoveis/terrenos

**Pré-requisitos:**
As bibliotecas:
Pandas,
Scrapy.
1º Criar ambiente virtual na pasta olxscraping com comando "python3 -m venv tutorial-env", o tutorial-env é o nome da pasta que vai criar e também o local a ser instalado.
2º Entrar no ambiente virtual com comando "cd /olxcraping/tutorial-env", "source tutorial-env/bin/activate"
3º instalar scrapy com comando "pip install Scrapy", é recomendado instalar no ambiente virtual.
4º instalar pandas com comando "pip install pandas"



## **WEBSCRAPING**
<p align="center"></p>

**Executando o código de webscraping:**
Abra o terminal e entre na pasta do projeto com:
```bash
cd /olxscraping
```
(local na minha máquina linux).

**Entre no ambiente virtual com:**
```bash
source venv/bin/activate
```

**Digite o código para iniciar e criar um csv:**
```bash
scrapy crawl olx -o olx.csv
```
Será criado o arquivo  na pasta olxscraping/webscraping
Será criado um arquivo csv nessa pasta com os dados.

## **ANÁLISE DE DADOS**
<p align="center"></p>


**Executando o código de análise de dados:**
<p>O código está em olxscraping/webscraping/olx_analise.py</p>
<p>Ele executará no arquivo 
olxscraping/webscraping/olx.csv que foi criado a partir da execução do webscraping.
Ao executá-lo pedirá para digitar 1 para só mostrar na tela as informações ou 0 para criar 7 arquivos csv na pasta olxscraping/webscraping.</p>
<p>
Obs.: Um bug acontece ao analisar o banco de dados criado, é preciso abrir o arquivo olx.csv e editar a última coluna "título", tirando o acento ficando "titulo".
</p>

**Resultados ao executar os códigos:**
Os meus arquivos que criei com o código está em olxscraping/webscraping/resultados se quiser já vê-los. É preciso colocar o arquivo olx.csv na pasta olxscraping/webscraping para o código de análise rodar.

**Informações sobre a análise:**
É feito a média, mínimo e máximo dos tamanhos e preços de cada região e a quantidade de anúncios por região.

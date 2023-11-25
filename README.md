## Webscraping e análise de dados com python

Os códigos fazem webscraping e análise dos dados adquiridos usando python.
O site é o de anúncios da Olx. A página dos terrenos é: https://sc.olx.com.br/florianopolis-e-regiao/imoveis/terrenos

**Pré-requisitos:**
As bibliotecas
Pandas,
Scrapy e o ambiente virtual.
<p>1º Criar ambiente virtual na pasta olxscraping com comando:</p>

``` bash
python3 -m venv .env
```
o "tutorial-env" é o nome da pasta que vai criar e também o local a ser instalado.
<p>2º Entrar no ambiente virtual com comando:<p/>

``` bash windows
source env/bin/activate
```

``` bash linux
source env/Scripts/activate
```
  
3º Instalar scrapy e pandas com comando: 
``` bash
pip install scrapy pandas
```
Obs.: é recomendado instalar no ambiente virtual.

## **WEBSCRAPING**
<p align="center"></p>

**Executando o código de webscraping:**
Abra o terminal e entre na pasta do projeto com:
```bash
cd desafio/olxscraping
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
Será criado o arquivo  na pasta olxscraping
Será criado um arquivo csv nessa pasta com os dados.

## **ANÁLISE DE DADOS**
<p align="center"></p>


**Executando o código de análise de dados:**
<p>O código está em olxscraping/olx_analise.py</p>
<p>Ele executará no arquivo 
olxscraping/olx.csv que foi criado a partir da execução do webscraping.
Ao executá-lo pedirá para digitar 1 para só mostrar na tela as informações ou 0 para criar 7 arquivos csv na pasta olxscraping.</p>
<p>
Obs.: Um bug acontece ao analisar o banco de dados criado, é preciso abrir o arquivo olx.csv e editar a última coluna "título", tirando o acento ficando "titulo".
</p>

**Resultados ao executar os códigos:**
Os meus arquivos que criei com o código está em olxscraping/resultados se quiser já vê-los. É preciso colocar o arquivo olx.csv na pasta olxscraping para o código de análise rodar.

**Informações sobre a análise:**
É feito a média, mínimo e máximo dos tamanhos e preços de cada região e a quantidade de anúncios por região.

# Trabalho Final - INE5454

Trabalho Final da Disciplina INE5454, feito por Arthur de Sousa Costa (Matrícula 20100515). Neste trabalho, foi desenvolvido um código capaz de coletar dados de um website que contém processos do MPSC. Tal base será utilizada para realizar experimentos iniciais em meu TCC e de colegas, referentes a textos jurídicos.

## Página a ser acessada

* [Clique aqui](https://transparencia.mpsc.mp.br/QvAJAXZfc/opendoc.htm?document=portal%20transparencia%5Cportal%20transp%20mpsc.qvw&lang=pt-BR&host=QVS%40qvias&anonymous=true)

## Atributos que foram extraídos (.csv)
* N. do Processo
* Assunto
* Classe
* Comarca
* Promotoria de Justiça
* Homologado pelo CSMP
* Data
* PDF (arquivo)
* Movimentação (link)

## Arquivo final

Um .csv contendo os atributos descritos acima.

```
result.csv
```

Um diretório contendo todos os PDFs existentes dos processos.

```
Diretório: PDFs
Cada .pdf é nomeado de acordo com o número de seu respectivo processo.
```

## Principais APIs utilizadas

* Selenium
* BeautifulSoup
* Requests

## Pré-requisitos

Abaixo, são descritos alguns pré-requisitos necessários para a execução do código.

### Chrome Driver

Como foi utilizado o framework Selenium para simular ação humana através do browser Google Chrome, é necessário o driver correspondente ao navegador utilizado. Atualmente, estou utilizando a versão 113 do Chrome, e seu respectivo driver está no mesmo path do código principal.

```
chromedriver.exe
```

Assim, é necessário verificar a versão do Chrome antes de executar o código e, se necessário, utilizar outro driver de acordo com a versão sendo utilizada.

### Bibliotecas

Foram utilizadas bibliotecas diversas para a realização deste trabalho. A fim de executar o código, é necessário instalar todos os requirements.

```
pip install -r requirements.txt
```

## Execução

```
python3 scrap_mpsc.py
```
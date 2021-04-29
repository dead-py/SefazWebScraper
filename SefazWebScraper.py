#!/bin/python3

import bs4 as bs
import requests
from termcolor import colored
from tabulate import tabulate

states = []
states.append(["Autorizador", "Autorização", "Retorno Autorização", "Inutilização", "Consulta Protocolo", "Status Serviço", "Tempo Médio", "Consulta Cadastro", "Recepção Evento"])
state = []
situations = []

url = "https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY="
page = requests.get(url)

soup = bs.BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all(class_='tabelaListagemDados')

for table in tables:
    rows = table.find_all('tr', recursive=False)

    for content in rows:
        state = []
        contents = content.find_all('td', recursive=False)

        for texto in contents:
            texto = str(texto).lstrip('<td>').rstrip('</td>').lstrip('img src="imagens/bola').rstrip('_P.png"').lstrip('pan>').rstrip('</sp')

            if texto == '_amarela':
                texto = colored('###', 'yellow')

            elif texto == '_verde':
                texto = colored('###', 'green')

            elif texto == '_vermelha':
                texto = colored('###', 'red')

            elif texto == '</spa':
                texto = colored('###', 'white')

            if texto == 'S':
                texto = 'SP'

            if not str(texto):
                texto = 'Null'

            state.append(texto)

        states.append(state)

states.remove([])
print(tabulate(states, headers='firstrow', tablefmt='grid'))


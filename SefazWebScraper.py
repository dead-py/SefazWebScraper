#!/bin/python3

import bs4 as bs
import requests



states = []
state = []
situations = []

url = "https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY="
page = requests.get(url)

soup = bs.BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all(class_='tabelaListagemDados')

for table in tables:
    rows = table.find_all('tr', recursive=False)
    
    for content in rows:
        
        states.append(state)
        state = []
        contents = content.find_all('td', recursive=False)
        
        for texto in contents:
            texto = str(texto).lstrip('<td>').rstrip('</td>')
            texto = str(texto).lstrip('img src="imagens/bola_').rstrip('_P.png"').lstrip('pan>').rstrip('</spa')
            #if texto == 'S':
            #    texto = 'SP'
                
            if not str(texto):
                texto = 'Null'
            
            state.append(texto)
            


states.remove([]);states.remove([])

for state in states:
    print(state)

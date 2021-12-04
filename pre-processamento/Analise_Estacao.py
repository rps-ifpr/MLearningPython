#Bibliotecas já instaladas no ambiente Python
import os
import time

#Importar as funções que iremos utilizar do Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Importando BeautifulSoup
from bs4 import BeautifulSoup

#Endereco do driver do browser de sua preferência
folder_chrome_driver='C:\\chromedriver.exe'

#Para desabilitar a abertura de uma nova janela do browser pelo Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")

#Configurando o Selenium
browser = webdriver.Chrome(options=chrome_options,executable_path=folder_chrome_driver)

#Atribuir ao Selenium o site que será acessado
browser.get('https://tempo.inmet.gov.br/TabelaEstacoes/')

#Recomendado para evitar ban do servidor
time.sleep(3)

#Selecionar em "Produto" a opção "Tabela de Dados das Estações"
browser.find_element_by_xpath("//select/option[@value='TabelaEstacoes']").click()

VALOR_ESTACAO='A801' #Porto Alegre - RS

DATA_INIT='22/11/2020'
DATA_END='22/01/2021'


#Selecionamos a opção de estação automática
browser.find_element_by_xpath("//select/option[@value='T']").click()

#Selecionamos qual estação estamos interessados
browser.find_element_by_xpath("//select/option[@value='"+VALOR_ESTACAO+"']").click()

#Primeiro limpados o formulário e então preenchemos com a data inicial que desejamos.

browser.find_element_by_id("datepicker_EstacoesTabela_Inicio").clear()
browser.find_element_by_id("datepicker_EstacoesTabela_Inicio").send_keys(DATA_INIT)

#O mesmo para a data final
browser.find_element_by_id("datepicker_EstacoesTabela_Fim").clear()
browser.find_element_by_id("datepicker_EstacoesTabela_Fim").send_keys(DATA_END)

#Por fim, clicamos em "gerar tabela"
browser.find_element_by_id("EstacoesTabela").click()

#Pedimos para o Selenium aguardar por alguns segundos até que a tabela seja gerada pelo site
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "tabela")))

#atribuimos a estrutura atual do site para uma variável para que o BeautifulSoup possa fazer sua mágica!
page_source = browser.page_source

#"Limpamos" a estrutura do site com o BeautifulSoup
soup = BeautifulSoup(page_source, 'lxml')

#Pede para retornar a tabela existente na tag "table"
table = soup.find('table')

import pandas as pd

# Converter a tabela html em Dataframe.
# Definimos como separador decimal ',' e milhar '.'
df = pd.read_html (str (table), decimal=',', thousands='.')[0]
df = pd.DataFrame (df.to_records ())

# Se preferir, também há como renomear o cabeçalho da planilha.

New_Names = ['index', 'Date', 'Time', 'Tinst', 'Tmax', 'Tmin', 'URinst', 'URmax', 'URmin', 'PtOrvalhoinst',
             'PtOrvalhomax', 'PtOrvalhmin',
             'Pinst', 'Pmax', 'Pmin', 'Vveloc', 'Vdir', 'Vraj', 'Rad', 'Precipt'
             ]

for n in range (0, len (df.keys ())):
    df = df.rename (columns={df.keys ()[n]: New_Names[n]})

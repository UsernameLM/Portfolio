import os, io
from selenium import webdriver
import time
import base64
import matplotlib.pyplot as plt
import numpy as np
import requests
import datetime as dt
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def check_status(): #Ver se está conectando com o site
    my_url = "https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/"
    response = requests.get(my_url)
    # Pega exceção e formata(conecta as strings)
    print("response.ok : {} , response.status_code : {}".format(response.ok, response.status_code))
    print("Preview of response.text : ", response.text[:500])

def create_graph():
    driver = webdriver.Chrome()
    # navegar pagina
    driver.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/")
    time.sleep(5)
    values = []
    values_usable = []
    # espera carregar a table
    table = driver.find_element(By.ID, "quotes_history")
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells:
            # extrair o primeiro e quarto valor e colocar eles em lista
            value_1 = cells[0].text.strip()
            value_2 = cells[1].text.strip()
            value_3 = cells[2].text.strip()
            value_4 = cells[3].text.strip()
            values.append([value_1, value_4])

    # pegar valor e converter em float e datas
    dates = [dt.datetime.strptime(value[0], '%d/%m/%Y') for value in values[1:]]
    value_2 = [float(value[1].replace(".", "").replace(",", ".")) for value in values[1:]]
    return dates, value_2, value_3, value_4

def save_image():
    fig = create_graph()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Pegar os arquivos no diretório do script, template no caso
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # especificando o caminho do script
    file_path = os.path.join(script_dir, 'graph.png')
    # salvando a imagem no diretorio
    plt.savefig(file_path)

def save_image64():
    date, variation, _1, _2 = create_graph()
    graph = plt.plot(date, variation)
    plt.title('Ibovespa Historical Data')
    plt.xlabel('Date')
    plt.ylabel('Variation(%)')
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d/%m'))
    #prevenir informações uma em cima da outra
    plt.xticks(rotation=45)
    # salvando como buffer, pois não funciona colocar no site a imagem
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # converter imagem em dado 64
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()

    return image_base64,date,variation


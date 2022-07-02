"""
Camila Ojeda 4 junio de 2022
"""

from os import path
from pathlib import PurePath
from bs4 import BeautifulSoup

import sys, re, requests, os

counter = 0

def get_html():

    # Se analizan todas las url indicadas en el archivo urls.txt, con el fin de obtimizar variables
    with open('/home/angie/Documents/git/Data_Analytics+Python/urls.txt', 'r') as fh:
        urls = fh.readlines()
    urls = [url.strip() for url in urls] # Se guarda linea por linea cada enlace del documento

    paths = download_html(urls, '.')
    
    for path in paths:
        get_document(path)

def download_html(urls, dir):
    paths = []

    for url in urls:
        file_name = PurePath(url).name # Se extrae el ultimo paramatro de la ruta para nombrar el archivo
        file_path = path.join(dir, file_name) # Se asigna el path
        text = ''

        try:
            response = requests.get(url) # Obtener datos de la url
            if response.ok:  # Si el proceso es exitoso (200)
                text = response.text # text es igual al código fuente de la pagina
            else:
                print('Mala respuesta para', url, response.status_code)
        except requests.exceptions.ConnectionError as exc:
            print(exc)
    
        with open(file_path, 'w') as fh: # Guardar el archivo con el nombre del path
            fh.write(text)

        paths.append(file_path) # Se crea un vector con todos los paths

    return paths

def get_document(path):
    global counter
    counter += 1
    local_counter = 0
    pos = []

    set_names()
    
    with open(path, 'r') as fh:
        content = fh.read()
    soup = BeautifulSoup(content, 'html.parser')

    content_class = soup.find_all("a", {"class": "btn btn-green btn-block"})
    content_class = str(content_class)
    local_counter = 0
    pos = []
    for i, char in enumerate(content_class):
        if char == '"':
            local_counter += 1
            if local_counter >= 3:
                pos.append(i)
                if local_counter == 4:
                    break
    link = content_class[pos[0]+1:pos[1]]
    print(type(link))
    print(link)
    response = requests.get(link)
    open(names_databases[counter-1],"wb").write(response.content)

def set_names():
    local_counter = 0
    names_databases = ["museos", "salas_de_cine", "bibliotecas_populares"]
    
    for i in names_databases:
        os.mkdir()
    
    from datetime import datetime
    date = datetime.now()
    month = date.strftime('%m')

    import datetime
    datetime_object = datetime.datetime.strptime(month, "%m")
    full_month_name = datetime_object.strftime("%B")



    from datetime import datetime
    for i in names_databases:
        names_databases[local_counter] = names_databases[local_counter] +"\$"+ date.strftime('%Y-') + full_month_name + names_databases[local_counter] + '-' + date.strftime('%D') + '-' + date.strftime('%M') + '-' + date.strftime('%Y') + '.csv'
        local_counter += 1

if __name__ == "__main__":
    args = sys.argv 

    if len(args) is 1:
      get_html()

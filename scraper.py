"""
Camila Ojeda 4 junio de 2022
"""

from os import path
from pathlib import PurePath
from bs4 import BeautifulSoup

import sys, re, requests, os, datetime

counter = 0

def get_html():

    # Se analizan todas las url indicadas en el archivo urls.txt, con el fin de optimizar variables
    with open('/home/angie/Documents/git/Data_Analytics+Python/urls.txt', 'r') as fh:
        urls = fh.readlines()

    paths = download_html(urls, '.')
    
    for path in paths:
        get_document(path)

def download_html(urls, dir):
    paths = []

    for url in urls:
        file_name = PurePath(url).name # Se extrae el ultimo paramatro de la ruta para nombrar el archivo
        file_path = path.join(dir, file_name) # Se asigna el path con el que será guardado
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
            fh.write(text) # se guarda el contenido html de cada enlace

        paths.append(file_path) # Se crea un vector con todos los paths

    return paths

def get_document(path):
    global counter
    counter += 1
    local_counter = 0
    pos = []

    paths, names_files = set_names() # Los valores que retornan, retornan a las variables correspondientes
    
    with open(path, 'r') as fh:
        content = fh.read()
    soup = BeautifulSoup(content, 'html.parser') # Se indica que se analizará un arhivo con contenido html

    content_class = soup.find_all("a", {"class": "btn btn-green btn-block"}) # se busca la clase btn btn-green btn-block en el archivo
    content_class = str(content_class) # se convierte a str la linea extraida del html
    local_counter = 0
    pos = []
    for i, char in enumerate(content_class): # como el fragmento que necesitamos está entre "" entones se cuentan y se extrae lo que me sierve
        if char == '"':
            local_counter += 1
            if local_counter >= 3:
                pos.append(i)
                if local_counter == 4:
                    break
    link = content_class[pos[0]+1:pos[1]] # Se extrae dependiendo de la posición
    response = requests.get(link)
    final_path = str(paths[counter-1] + '/' + names_files[counter-1]) # se concatena como string el path donde se guardará el archivo

    if not os.path.exists(paths[counter-1]): # Si el direcotrio no existe creelo
        os.makedirs(paths[counter-1])
        open(final_path,"xb").write(response.content) # se guarda el archivo

    else: # Si los direcotrios existen, solamente se reemplara el archivo
        open(final_path,"wb").write(response.content)
    


def set_names(): # Asignar el nombre de cada archivo
    paths = []
    names_files = []
    names_databases = ["museos", "salas_de_cine", "bibliotecas_populares"]

    date = datetime.datetime.now()
    month = date.strftime('%m') # Traer el número del mes actual
    datetime_object = datetime.datetime.strptime(month, "%m")
    full_month_name = datetime_object.strftime("%B") # Convertir el número del mes al nombre del mes

    for i in names_databases:
        paths.append(i + '/' + date.strftime('%Y-') + full_month_name) # crear un vector con la ruta "museos/año-nombre de mes"
        names_files.append(i + '-' + date.strftime('%d') + '-' + date.strftime('%m') + '-' + date.strftime('%Y') + '.csv') # crear el nombre del archivo .csv

    return paths, names_files # retornar los dos valores anteriores

if __name__ == "__main__":
    args = sys.argv 

    if len(args) == 1:
      get_html()

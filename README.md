# Data Analytics + Python

El objetivo es crear un proyecto que consuma datos desde 3 fuentes distintas para popular una base de datos SQL con información cultural sobre bibliotecas, museos y salas de cines argentinos.

Este proyecto debe cumplir una seríe de requerimientos funcionales, estos se dividen en 4 partes fundamentales:

**Archivos fuente:** En esta fase se deberan obtener los archivos fuente utilizando la librería requests y serán almacendos de forma local.

**Procesamiento de datos:** En esta fase se procesan los datos para transformar los datos de los archivos fuente en la información que va a nutrir la base de datos.

Y finalmente la creación de las bases de datos y la actualización de estas, las cuales deben cumplir con una serie de requisitos, para más información y detalle de cada fase del proyecto consultar [este enlace](https://drive.google.com/file/d/1ZxBnjsof8yCZx1JVLVaq5DbRjvIIvfJs/view "Detalles de reto Alkemy").

___

# PRIMERA FASE: Archivos fuente

Para empezar con esta fase se consideró importante crear un archivo [txt](./urls.txt) que contenga los enlaces que el programa deberá consultar, para posteriormente descargar los archivos.

en este caso los enlaces a consultar son los siguientes:

- https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d

- https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae

- https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7


El programa consulta el archivo txt y guarda en un array los enlaces del archivo, como se muestra en la siguiente imagen, luego se llama a una función con el nombre *download_htmls* para extraer y almacenar en el array **paths** el contenido html de cada enlace.

<p align="center"> <img src=./imagenes/get_html.png> </p>

La funcion *download_htmls* se hace un requests a cada enlace y se almacena en la variable *paths* el contenido html de cada fuente.

<p align="center"> <img src=./imagenes/download_htmls.png> </p>

Ahora la variable *paths* de la imagen anterior se retorna nuevamente a la primera función (get_html).

<p align="center"> <img src=./imagenes/get_html_2.png> </p>

Ahora bien, si nos dirigimos a cada uno de los enlaces, como primra vista encontraremos que hay un boton descargar, el cual directamente va a la descarga del documento base para llenar la base de datos, esto ocurre con todos los enlances.

<p align="center"> <img src=./imagenes/vista_pag.png> </p>

Ahora se consulta el código fuente de la pagina, y se ubica el código del botón verde que indica la descarga en el html, como se observa a continuación.

<p align="center"> <img src=./imagenes/html_pag.png> </p>

Lo que realmente nos interesa es el enlace que directamente nos lleve a la descarga del archivo, entonces mediante el código vamos a ubicar en el html lo que nos interesa.

Antes de continuar, el código debe crear las rutas donde se guardarán los archivos .csv, estos deben quedar en rutas como se indica en el documento. 

<p align="center"> <img src=./imagenes/recorte.png> </p>

Para crear los nombres dependiendo la fecha, se realiza el siguiente código

<p align="center"> <img src=./imagenes/crear_rutas.png> </p>

Finalmente mediante la libreria *BeautifulSoup* se busca en el html el fragmento de código que redirecciona al enlace de la descarga, entonces se agrega la siguiente linea, donde se ezpecifica exactamente que parte del código html necesito buscar.

<p align="center"> <img src=./imagenes/extraer.png> </p>

<p align="center"> <img src=./imagenes/html.png> </p>

Luego se extrae de las "" el enlace y se guarda el documento, y finalmente en los direcotrios mensionados anteriormente se guardan los archivos, el código completo de esta primera fase se encuentra dando click [aquí](./scraper.py). 
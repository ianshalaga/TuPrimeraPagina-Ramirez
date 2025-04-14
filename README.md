# TuPrimeraPagina+Ramirez

Tercer desafío entregable del curso de Python en modalidad Flex de CoderHouse.

## Consigna

Crea una web en **Django** utilizando _herencia de plantillas_, con un modelo de por lo menos _3 clases_, _un formulario para ingresar datos a las 3 clases_ y _un formulario para buscar algo en la BD_, no hace falta que sea sobre las tres clases, con realizar búsqueda sobre una alcanzará.

Te sugerimos que hagas una web estilo _blog_ para ir preparando en la entrega final.

## Objetivos

Desarrollar tu primer sitio web en **Django** utilizando patrón **MVT**.

## Requisitos

- [x] Link de **GitHub** con el proyecto totalmente subido a la plataforma.
- Proyecto web **Django** con patrón **MVT** que incluya:
  - [x] Herencia de **HTML**.
  - [x] Por lo menos 3 clases en **models**.
  - [x] Un formulario para insertar datos a cada **model** creado.
  - [x] Un formulario para buscar algo en la **DB**.
  - [x] README que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

## Formato

Link al repositorio de **GitHub** con el nombre “TuPrimeraPagina+Apellido” por ejemplo “TuPrimeraPagina+Fernandez”.

<!-- ## Módulos (internos) -->

## Paquetes (externos)

- [Django](https://www.djangoproject.com/): es un framework web de alto nivel para Python, diseñado para desarrollar sitios web de forma rápida, segura y con buenas prácticas desde el inicio.

## Utilización

- Clone [este repositorio](https://github.com/ianshalaga/TuPrimeraPagina-Ramirez.git) en su ordenador:

> `git clone https://github.com/ianshalaga/TuPrimeraPagina-Ramirez.git`

- Posiciónese en el directorio del proyecto y cree un entorno virtual:

> `python -m venv .venv`

- Active el entorno virtual:

> `.venv\Scripts\activate`

- Instale los paquetes necesarios:

> `pip install -r requirements.txt`

## Descripción

Las rutas del proyecto son:

- Página principal: `dominio/`
- Administración: `dominio/admin/`
- Pestaña **Música**: `dominio/music/song` (formulario de búsqueda `GET`)
- Agregar nueva canción: `dominio/music/song-create` (formulario de creación `POST`)

Se puede consultar el archivo `sc_ost.plantuml` para corroborar el diagrama de clases de los modelos de la aplicación `Music`.

Se incluye la pequeña base de datos en el respositorio para que se vizualicen algunos ejemplos de canciones cargadas.

from fastapi import FastAPI
from routers import products, app
from fastapi.staticfiles import StaticFiles

main = FastAPI()

#Routers
main.include_router(products.productos)
main.include_router(app.app)
#La función mount sirve para poder cargar archivos de tipo esticos,es decir poder cargar informarción de archvios como imagenes, archvios html, archvios css, entre otros
main.mount("/img", StaticFiles(directory="static"), name= "static")
#Para esta funcion se pasa primero la ruta la cual se define para acceder a los archicos estaticos
#Segundo se pasa el nombre del directorio por el cual se cargan los archivos
#tercero se pasa un nombre por el cual se puede llamar


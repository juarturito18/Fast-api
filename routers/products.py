#En esta caso importamos apirouer, debido a quenos ayuda  apoder tener una api principal que conecte con todas las apis que se usen en el proyecto
from fastapi import APIRouter, HTTPException

#Este router se usa de la misma manera, que el FastAPI(), con la diferencia de que en este archivo no es el que se crea el serviudo de uvicorn, sino que se crea en un archivo principal donde se crea
#Con el fin de llevar todas las rutas y poder tener arcivos independientes sin tener problemas de tener que juntar todo en un mismo archivo
productos = APIRouter(prefix="/product", #El prefix se utiliza para tener una refercia fija a donde va aapuntar la url por defecto
                      tags= ["Products"], #El tag lo que hace es que al tener la documentacion del api ya sea en swagguer o en otro programa nos separa los diferentes routers que usemos
                      responses={404:{"message":"No encontrado"}}) #ESto es para indicar la respuesta or defecto del problema en caso de algun error del sistema 

list_product =["Manzana", "Pera", "Naranja", "Uvas","Melon"]

@productos.get("/") # Aqui ya estamos indicando que por defecto se va referiar a la ruta de http://127.0.0.1:8000/product 
async def show_prodcut(): 
    return list_product

@productos.get("/{id}")
async def search_product(id:int):
    try:
        return list_product[id]
    except:
        raise HTTPException(status_code=204, detail= "La lista de producto no es tan grande para contener un producto en este indice")
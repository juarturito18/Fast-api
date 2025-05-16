from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

app = APIRouter(tags=["user"])

#metodo get
#El metodo get basicamente en lo que nos ayuda a poder leer información de la web 
@app.get("/")# ESta es la ruta de get por defeto "/" es decir http://127.0.0.1:8000
async def show():
    return "Hello word"

class User(BaseModel):
    id : int
    name: str
    url: str
    age: int

users_list = [User(id = 1, name ="Juan", url ="http://127.0.0.1:8000", age =18),
              User(id = 2, name ="Jorge", url ="http://127.0.0.1:8000", age =20),
              User(id = 3, name ="Silvana", url ="http://127.0.0.1:8000", age =47)]

@app.get("/app")
async def print():
    return [{"name": "Juan"},{"name": "Jorge"}, {"name": "Silvana"}]
#Para activar nuestro servidor en local usamos un el servidor por defecto de fastapi que es uvicorn y para ello escribimos en la linea de comando es  "uvicorn app:app --reload"
#http://127.0.0.1:8000 este vendria ser el servidor local de nuestro pc que solo podra ser util dentro de nuestro pc, que solo sera útil cuando este el codigo activo
#http://127.0.0.1:8000/docs es una forma de docuemtnar nuestro odifo de forma dinamica segun lo que creamos en el de las rutas

@app.get("/users")
async def user():
    return users_list

#path
@app.get("/users/{id}")
async def user(id:int):
    return search_user(id)

#query    
@app.get("/users/")
async def user(id:int):
    return search_user(id)

#Metodo post
#Con este metodo tenemos la facilidad de poder crear información para nuestra api o insertar valores
@app.post("/user/",status_code = 201) #Aqui podemos especificar el tipo de status code que quiero que aparezaca en este caso espeficiamos el 201 que indica que se a creado un contenido
async def user (user:User):
    if search_user(user.id):
        raise HTTPException(status_code = 204,detail="El ususario ya existe" ) #El HTTPException no sisrve para poder describir el problema de un del status code que nostros quermaos pra un problema
    else:
        users_list.append(user)

#Metodo put

@app.put("/user/")
async def user(user : User):
    for i, s_user in enumerate(users_list):
        if s_user.id == user.id:
            users_list[i] = user 
            return users_list[i]
    return {"Error": "No hay usuario con este id"}

@app.delete("/user/{id}")
async def user(id:int):
    for i, s_user in enumerate(users_list):
        if s_user.id == id:
            del users_list[i]
            return users_list
    return {"Error":"No existe usuario con este id"}


 
#Con este metodo 

def search_user(id:int):
    for user in users_list:
        if user.id == id:
            return user
    return None

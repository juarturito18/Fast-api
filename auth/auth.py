from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

auth = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Modelos
class User(BaseModel):
    username: str
    age: int
    email: str

class UserDB(User):
    password: str

# Base de datos simulada
DB = {
    "juan": {
        "username": "juan",
        "age": 18,
        "email": "juan@gmail.com",
        "password": "1232"
    },
    "jorge": {
        "username": "jorge",
        "age": 28,
        "email": "jorge@gmail.com",
        "password": "1234"
    }
}

def search_user(name: str):
    if name in DB:
        return UserDB(**DB[name])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El usuario no está autenticado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user

@auth.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = search_user(form.username)
    if not user:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    if form.password != user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    return {"access_token": user.username, "token_type": "bearer"}

@auth.get("/user/me")
async def me(user: UserDB = Depends(current_user)):
    return User(**user.dict())

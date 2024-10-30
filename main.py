from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from faker import Faker
from typing import List
from hashlib import sha256
import secrets

app = FastAPI()
security = HTTPBasic()
fake = Faker()

correct_username = "meu_usuario"
correct_password_hash = sha256("minha_senha".encode()).hexdigest()

def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    hashed_input_password = sha256(credentials.password.encode()).hexdigest()
    if credentials.username != correct_username or not secrets.compare_digest(hashed_input_password, correct_password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return credentials.username

@app.get("/names", response_model=List[str])
async def get_names(username: str = Depends(verify_password)):
    return [fake.name() for _ in range(10)]

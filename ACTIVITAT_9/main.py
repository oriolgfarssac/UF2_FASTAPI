from fastapi import FastAPI
from crud import read_table
from schema import UserDefault

app = FastAPI()

@app.get("/users/", response_model=list[UserDefault])
def get_users():
    return read_table()
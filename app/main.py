from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola Mundo"}


@app.get("/hello")
def read_root():
    return {"message": "Hello world"}




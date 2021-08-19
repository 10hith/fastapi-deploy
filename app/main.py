from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_main():
    return {"lohith says": "got https working MF"}

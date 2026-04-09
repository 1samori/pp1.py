from fastapi import FastAPI

app = FastAPI()

@app.get("/get")
def geteo():
    return {"Hola":"Mundo"}

@app.post("/post")
def posteito():
    return {"ola":"Mundopost"}

@app.put("/put")
def pongo():
    return {"ola":"putMundo"}

@app.delete("/delete")
def deleteo():
    return {"chau":"Mundo"}

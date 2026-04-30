from fastapi import FastAPI,Path,Query,Body

app = FastAPI()

app.title = "CelularesTienda"

celulares = [{"id" : 1,"nombre": "Samsung J7","marca" : "Samsung","precio" : 1500000,"activo" : True},
            {"id" : 2,"nombre": "Moto G15","marca" : "Motorola","precio" : 400000,"activo" : True},
            {"id" : 3,"nombre": "Iphone 15","marca" : "Apple","precio" : 2000000,"activo" : True}]





@app.get("/celulares/{id}")
async def obtenerCelularesId(id : int = Path(...,gt=0)):
    for celular in celulares:
        if celular["id"] == id:
            return celular
    return {"detalle" : "celular no encontrado"}


@app.get("/celulares")
async def ObtenerCelularesActivos(activo : bool = Query(True)):
    celularesActivos = []
    for celular in celulares:
        if celular["activo"] == activo:
            celularesActivos.append(celular)
    return celularesActivos


@app.post("/celulares")
async def postCelular(
    id : int = Body(gt=0),
    nombre : str = Body(min_length = 1,max_length =50),
    marca :  str = Body(min_length = 1,max_length =50),
    precio : float = Body(gt = 0),
    activo : bool = Body(True)
):
    
    nuevoCelular = {
        "id" : id,
        "nombre": nombre,
        "marca" : marca,
        "precio" : precio,
        "activo" : activo,
    }
    celulares.append(nuevoCelular)
    return nuevoCelular

@app.put("/celulares/{id}")
async def modificarCelular(
    id : int = Path(gt=0),
    nombre : str = Body(min_length = 1,max_length =50),
    marca :  str = Body(min_length = 1,max_length =50),
    precio : float = Body(gt = 0),
):
    for celular in celulares:
        if celular["id"] == id:
            celular["nombre"] = nombre
            celular["marca"] = marca
            celular["precio"] = precio
            return celular
    return {"detalle" : "celular no encontrado"}

@app.delete("/celulares/{id}")
async def borrarCelular(id : int,activo : bool = Query(default = False)):
    for celular in celulares :
        if celular["id"] == id:
            if celular["activo"] == True:
                celular["activo"] = False
            else:
                celulares.remove(celular)
            return {"detalle" : "borrado"}
    return {"datelle" : "celular no encontrado"}

 

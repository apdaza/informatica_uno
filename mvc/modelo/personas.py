import pymongo
from bson import ObjectId

HOST = "127.0.0.1"
PORT = "27017"
DATABASE = "mvc"
COLLECTION = "personas"
URI_CONECTION = "mongodb://" + HOST + ":" + PORT + "/"

def get_all():
    data = {}
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {}
        resultado = coleccion.find(condicion)
        data = resultado
    except Exception as error:
        print("Error consultado datos", error)
    finally:
        return data

def get_one(id):
    data = {}
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id':ObjectId(id)}
        resultado = coleccion.find_one(condicion)
        data = resultado
    except Exception as error:
        print("Error consultado datos", error)
    finally:
        return data

def add_one(data):
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        coleccion.insert_one(data)
    except Exception as error:
        print("Error insertando datos", error)

def update_one(id, data):
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id':ObjectId(id)}
        valores = {'$set': data}
        coleccion.update_one(condicion, valores)
    except Exception as error:
        print("Error actualizando datos", error)

def delete_one(id):
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id':ObjectId(id)}
        coleccion.delete_one(condicion)
    except Exception as error:
        print("Error borrando datos", error)
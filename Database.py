from pymongo import MongoClient, database
from modelo import DataContinente, DataSurAmerica
from decouple import config

DATABASE = {
    "mongo_url": config("MONGO_URL"),
    "db_name": config("DB_NAME"),
}

client = MongoClient(DATABASE["mongo_url"])
database= client[DATABASE["db_name"]]

def get_mongo_database() -> database.Database:
    return database

coleccion=database.CovidCases

async def fetch_all_datacontinente():
    dataContinente=[]
    cursor= coleccion.aggregate([
        {"$unwind" :{
            "path" : "$data",
            "includeArrayIndex" : "ix"
        }},
        {"$group":{
            "_id": '$continent',
            "casos_totales": {"$sum" : '$data.new_cases'},
            "nro_muertes_totales":{"$sum" : '$data.new_deaths'}
        }
        },
        {"$addFields":{
            "continente":'$_id'
            }
        }        
    ])

    for document in cursor:
        print(document)
        dataContinente.append(DataContinente(**document))
    return dataContinente

async def fetch_all_datasuramerica():
    dataSurAmerica=[]
    cursor= coleccion.aggregate([
    {
        '$unwind': {
            'path': '$data', 
            'includeArrayIndex': 'ix'
        }
    }, {
        '$match': {
            'continent': 'South America'
        }
    }, {
        '$group': {
            '_id': '$location', 
            'casos_totales': {
                '$sum': '$data.new_cases'
            }, 
            'nro_muertes_totales': {
                '$sum': '$data.new_deaths'
            }
        }
    }, {
        '$addFields': {
            'pais': '$_id'
        }
    }
    ])
    for document in cursor:
        dataSurAmerica.append(DataSurAmerica(**document))
    return dataSurAmerica
from fastapi import FastAPI
from fastapi.testclient import TestClient
from Database import(
    fetch_all_datacontinente,
    fetch_all_datasuramerica,
    get_mongo_database
)

app = FastAPI(
    title="Api LabDataBase",
    description="An api for covid data visualization",
)

@app.get("/Api/DataContinente")
async def get_DataPais():
    response= await fetch_all_datacontinente()
    return response
@app.get("/Api/DataSuramerica")
async def get_DataPais():
    response= await fetch_all_datasuramerica()
    return response

#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         schema_extra = {
#             "example": {
#                 "continente": "Asia",
#                 "pais": "Afganistan",
#                 "casosTotales": "5",
#                 "muertesTotales": "5",
#             }
#         }

# @app.get("/")
# async def root():
#     db = get_mongo_database()
#     collection= db.CovidCases
#     agg_result=collection.aggregate([
#         {"$unwind" :{
#             "path" : "$data",
#             "includeArrayIndex" : "ix"
#         }},
#         {"$group":{
#             "_id": '$continent',
#             "casos_totales": {"$sum" : '$data.new_cases'},
#             "nro_muertes_totales":{"$sum" : '$data.new_deaths'}
#         }
#         },        
#     ])
#     return agg_result
    


# @app.on_event("startup")
# def startup():
#     database = get_mongo_database()
#     data= list(database.CovidCases.find())
#     return data

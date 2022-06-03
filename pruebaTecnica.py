import csv
from csv import writer
import pymongo   #importa la libreria de pymongo


cliente= pymongo.MongoClient( "mongodb://localhost:27017/") # se hace la conexion con la base de datos
# se guarda en la variable cb la base de datos y en la variable coleccion la coleccion con la que se va a trabajar
db = cliente[ "data_prueba_tecnica"]
coleccion = db[ "pruebat"]
# se recorre con un for toda la coleccion y se almacena en la variable x
for x in coleccion.find({},{"id":3,"nombre":1}):
    print(x)
    
with open('prueba.csv','a',newline='')as csvfile:
    writer = csv.writer(csvfile,delimiter = ',')
    writer.writerow(x)


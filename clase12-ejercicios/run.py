import json
import pandas
import couchdb
from couchdb import Server, Session

"""

user = "Carlos Castillo"
password = "Tlca2407"
couchserver = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password))

origen: https://gist.github.com/marians/8e41fc817f04de7c4a70
"""
usuario = 'Carlos Castillo'
clave = 'Tlca2407'

s = Server('http://%s:%s@localhost:5984/'% (usuario, clave))
db = s.create('matimonios2014')
data = pandas.read_csv('Matrimonios2014_1000.csv')
datos_json = data.to_json(orient='index')
datos_json_1 = json.loads(datos_json)
[db.save(datos_json_1[d]) for d in datos_json_1]


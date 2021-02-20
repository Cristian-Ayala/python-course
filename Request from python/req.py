# For a couchDB server an database.
import requests

url = 'http://localhost:5984/clientes/_find'
params = {"selector": {}}
headers = {'Content-Type': 'application/json; charset=utf-8'}
print(params, "\n")
print(headers, "\n")
r = requests.post(url=url,
                  headers=headers,
                  auth=('admin', 'admin'),
                  json=params)
response = r.json()
print(response)

# ------------------------ couchDB answer ------------------- 
# {
#     'docs': [{
#         '_id': '176bd7358046032d7b459961dc0001cb',
#         '_rev': '7-8cc9bec11e44a7bef81ced1e98553d72',
#         'nombreCompleto': 'Andrea Lopez Guevara',
#         'telefonoCasa': '2422-890',
#         'celular': '7190-2120',
#         'whatsapp': '7200-2398',
#         'direccion': 'Colonia España, pasaje H poligono 3',
#         'municipio': 'Chalchuapa',
#         'departamento': 'Santa Ana',
#         'puntoDeReferencia': 'Calle trapiche',
#         'observaciones': '',
#         'fechaRegistro': '2020-07-08T21:55:18.859+00:00'
#     }, {
#         '_id': '1e27dcc7529ef95ddd806aa8be003b8c',
#         '_rev': '1-51446a4e86b2f566021b9fc7ef916ab9',
#         'nombreCompleto': 'Juanita',
#         'telefonoCasa': '32343242',
#         'celular': '32132132',
#         'whatsapp': '32131231',
#         'direccion': 'calle al cementerio',
#         'departamento': 'santa ana ',
#         'municipio': 'jdksadkh'
#     }, {
#         '_id': '2269fc1c847d0a718a6101833d004f12',
#         '_rev': '4-11a8b145e574c357980d3729ea3b8481',
#         'nombreCompleto': 'David Jesús Guzmán',
#         'telefonoCasa': '2434-2323',
#         'celular': '0',
#         'whatsapp': '0',
#         'direccion': 'Colonia Jardines del tecana pasaje B casa 22',
#         'municipio': 'Santa Ana',
#         'departamento': 'Santa Ana',
#         'puntoDeReferencia': 'a la par de la iglesia Bautista',
#         'observaciones': '',
#         'fechaRegistro': '2020-06-08T21:55:18.859+00:00'
#     }, {
#         '_id': '2269fc1c847d0a718a6101833d006216',
#         '_rev': '5-cd890e8694a9f1a249fc3617e9d92b74',
#         'nombreCompleto': 'Claudia Teresa Martinez',
#         'telefonoCasa': '2434-2323',
#         'celular': '7775-7777',
#         'whatsapp': '7234-2343',
#         'direccion': 'Colonia Lamatepec, pasaje el jocote casa 24B',
#         'municipio': 'Santa Ana',
#         'departamento': 'Santa Ana',
#         'puntoDeReferencia': '',
#         'observaciones': '',
#         'fechaRegistro': '2020-07-08T21:55:18.859+00:00'
#     }, {
#         '_id': '4f440227907d3574ebca0281f0004dce',
#         '_rev': '1-c6fc75fca7c6fa96247af4fd7c9e9683',
#         'nombreCompleto': 'Francisco Flores Perez',
#         'telefonoCasa': '2343-1233',
#         'direccion': 'Final calle el mango casa 32',
#         'departamento': 'santa ana',
#         'municipio': 'Santa Ana'
#     }],
#     'bookmark':
#     'g1AAAABweJzLYWBgYMpgSmHgKy5JLCrJTq2MT8lPzkzJBYormKSZmBgYGZlbGpinGJuam6QmJScaGFkYphkYGJikJKeC9HHA9BGlIwsAcTsdlQ',
#     'warning':
#     'No matching index found, create an index to optimize query time.'
# }

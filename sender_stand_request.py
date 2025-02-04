import configuration
import data
import requests

def post_create_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             headers=data.headers) #el que recibe esta informacion devuelve el token.

def post_new_client_kit(kit_body, authToken):
    current_headers = data.headers.copy()  #referenciar y copiar los headers
    current_headers["Authorization"] = "Bearer " + authToken #llamar el current y agrega la nueva llave authToken
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers) #el token lo insertamos a este diccionario headers




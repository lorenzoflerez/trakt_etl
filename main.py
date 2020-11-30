import json

import requests
import boto3
from datetime import datetime


headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': 'c444ed982a7692768e7389d1e6e845aba1f19a428c36e9e2c33d3586de027bb6'
}

list_trending = requests.get('https://api.trakt.tv/lists/trending', headers=headers)


## Metodo para pedir las listas trending,describir las movies de la lista, y el summary de las peliculas
## todo compilado en un solo json
## esta quemado el rango para por que la ejecucion es lenta
##len(list_trending.json()) len(list_trending.json())-1
def list_movies_summary(head):
    for i in range(len(list_trending.json())):
        idd_list = list_trending.json()[i]['list']['ids']['trakt']
        url_id_list = 'https://api.trakt.tv/lists/{id}/items/movies'.format(id=idd_list)
        item = requests.get(url_id_list, headers=head)

        print('Get Sumary_movies from list')
        summary_movie = summary_movies(item.json())
        if i == 0:
            result = '[' + '{"list_info":{"movies_summary":' + summary_movie + ',"listid":"' + str(idd_list) + '"}}'
        elif i == len(list_trending.json())-1:
            result += ']'
        else:
            result += ',{"list_info":{"movies_summary":' + summary_movie + ',"listid":"' + str(idd_list) + '"}}'

    return result


##Metodo para bajar de la api el summary de una pelicula, se crea un json con los sumarys de las peliculas de una lista
## Esta limitado para probar que mando el tamaño de los datos, por que si no el tiempo de ejecucion es muy largo
##len(item_json) len(item_json) - 1
##
def summary_movies(item_json):
    for i in range(len(item_json)):
        id_movie = item_json[i]['movie']['ids']['trakt']
        url_summary_movie = 'https://api.trakt.tv/movies/{id}?extended=full'.format(id=id_movie)
        summary_movie = requests.get(url_summary_movie, headers=headers)
        if i == 0:
            texts = '[' + summary_movie.text
        elif i == len(item_json) - 1:
            texts += ']'
        else:
            texts += ',' + summary_movie.text
    return texts


def people_movies_list(head):
    for i in range(len(list_trending.json())):
        idd_list = list_trending.json()[i]['list']['ids']['trakt']
        url_id_list = 'https://api.trakt.tv/lists/{id}/items/movies'.format(id=idd_list)
        item = requests.get(url_id_list, headers=head)
        id_movie = item.json()[i]['movie']['ids']['trakt']

        print('Get People from Movies_List')
        summary_movie = people_movies(item.json())
        if i == 0:
            result = '[' + '{"list_info":{"peoples":' + summary_movie + ',"listid":"' + str(
                idd_list) + '","id_movie":' + str(id_movie) + '}}'
        elif i == len(list_trending.json()) - 1:
            result += ']'
        else:
            result += ',{"list_info":{"peoples":' + summary_movie + ',"listid":"' + str(
                idd_list) + '","id_movie":' + str(id_movie) + '}}'

    return result


def people_movies(item_json):
    for i in range(len(item_json)):
        id_movie = item_json[i]['movie']['ids']['trakt']
        url_summary_movie = 'https://api.trakt.tv/movies/{id}/people'.format(id=id_movie)
        summary_movie = requests.get(url_summary_movie, headers=headers)
        if i == 0:
            texts = '[' + summary_movie.text
        elif i == len(item_json) - 1:
            texts += ']'
        else:
            texts += ',' + summary_movie.text
    return texts


## metodo para subir a s3
def upload_s3(endpoint, Body, nameFile):
    now = str(datetime.now())[0:16]
    s3 = boto3.client('s3')
    s3.put_object(Body=Body, Bucket='proyecto.final.pruebas',
                  Key="{date}/prueba/{endpoint}/{namefile}".format(date=now, endpoint=endpoint, namefile=nameFile))


##s cadena con la informacion json de la descripcion de peliculas)
movies = list_movies_summary(headers)
upload_s3('list_sumamry_movies',movies,'movies.json')

print('Ok: upload movies in s3')


peoples_movies = people_movies_list(headers)
upload_s3('people_movies_list', peoples_movies, 'peoples_movies.json')

print('Ok: upload peoples in s3')

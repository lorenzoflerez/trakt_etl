import json

import requests
import boto3
from datetime import date

headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': 'c444ed982a7692768e7389d1e6e845aba1f19a428c36e9e2c33d3586de027bb6'
}



##len(list_trending.json()) len(list_trending.json())-1
def list_movies_summary(head):
    list_trending = requests.get('https://api.trakt.tv/lists/trending', headers=head)
    for i in range(2):
        idd_list = list_trending.json()[i]['list']['ids']['trakt']
        url_id_list = 'https://api.trakt.tv/lists/{id}/items/movies'.format(id=idd_list)
        item = requests.get(url_id_list, headers=head)

        print('Get Sumary_movies from list')
        summary_movie = summary_movies(item.json())

        if i == 0:
            result = '[' + '{"list_info":{"movies_summary":' + summary_movie + ',"listid":"' + str(idd_list) + '"}}'
        elif i == 2-1:
            result += ']'
        else:
            result += ',{"list_info":{"movies_summary":' + summary_movie + ',"listid":"' + str(idd_list) + '"}}'

    return result

##len(item_json) len(item_json) - 1
def summary_movies (item_json):

    for i in range(10):
        id_movie = item_json[i]['movie']['ids']['trakt']
        url_summary_movie = 'https://api.trakt.tv/movies/{id}?extended=full'.format(id=id_movie)
        summary_movie = requests.get(url_summary_movie, headers=headers)
        if i == 0:
            texts = '[' + summary_movie.text
        elif i == 10-1:
            texts += ']'
        else:
            texts += ',' + summary_movie.text
    return texts

def upload_s3(endpoint,Body ):
    s3 = boto3.client('s3')
    s3.put_object(Body=Body, Bucket='proyecto.final.pruebas', Key="{date}/prueba/{endpoint}/movies.json".format(date=date.today(),endpoint=endpoint))

s = list_movies_summary(headers)
upload_s3('list_sumamry_movies',s)



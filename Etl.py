import boto3
import pandas as pd
import json
import pymysql
from datetime import datetime

s3 = boto3.client('s3')
invokelambda = boto3.client('lambda', region_name='us-east-2')


##funcion para invocar otras funciones lambdas
def invoke_lambda(json, functionName):
    resp = invokelambda.invoke(FunctionName=functionName, InvocationType='RequestResponse', Payload=json)
    print(resp['Payload'].read())


## lamba function 1 : extrat
def Extract_json_from_S3(bucket):
    list = s3.list_objects(Bucket=bucket)['Contents']
    ## solo se busca extraer el ultimo archivo guardado en s3
    ## suponiendo que los adatos anteriores ya han sido leido.
    key = list[0]['Key']
    response = s3.get_object(Bucket=bucket, Key=key)
    movies_json = '{"bucket_info":' + response['Body'].read().decode('utf-8') + ',"api_download":"' + str(
        list[0]['LastModified']) + '"}'
    return movies_json
    ##movies_json =json.loads(response['Body'].read().decode('utf-8'))
    ##invoke_lambda(movies_json,'function2')
    # return  movies_json


def filter_json_info(json):
    movies_json = json['bucket_info']
    api_download = json['api_download']
    for i in range(len(movies_json)):
        movie_info = movies_json[i]['list_info']['movies_summary']
        movies_info_df = filter_info_movies(movie_info, api_download)
        movies_info_df = movies_info_df.append(movies_info_df)
    return movies_info_df


# download_api : momento en el que se baja la informacion de la api
def filter_info_movies(movies_info, download_api):
    movies_info_df = pd.DataFrame(
        columns=(
        'title', 'year', 'id_movie', 'overview', 'released', 'country', 'language', 'genres', 'runtime', 'rating'
        , 'votes', 'comment_count', 'updated_at', 'translated', 'download_api'))

    for j in range(len(movies_info)):
        summary = movies_info[j]

        movies_info_df = pd.DataFrame(
            [[summary['title'], summary['year'], summary['ids']['imdb'], summary['overview'],
              summary['released'], summary['country'], summary['language'], summary['genres'], summary['runtime'],
              summary['rating'],
              summary['votes'], summary['comment_count'], summary['updated_at'], summary['available_translations'],
              download_api]],
            columns=['title', 'year', 'id_movie', 'overview', 'released', 'country', 'language', 'genres', 'runtime',
                     'rating', 'votes', 'comment_count', 'updated_at', 'translated',
                     'download_api']).append(
            movies_info_df)

    movies_df = movies_info_df
    return movies_df


def change_type_data(movies_df):
    now = datetime.now()
    movies_df2['download_api'] = pd.to_datetime(movie_df['download_api'])
    movies_df2['update_to_bd'] = pd.to_datetime(now)

    movies_upload = (movies_df2[['title', 'year', 'id_movie', 'overview', 'language', 'download_api', 'update_to_bd']])

    stad_upload = (movies_df2[['title', 'id_movie', 'released', 'country', 'genres', 'runtime',
                               'rating', 'votes', 'comment_count', 'updated_at', 'translated',
                               'download_api', 'update_to_bd']])
    update_info_bd(movies_upload)
    update_info_bd(stad_upload)


def update_info_bd(movies_df):
    cols = "`,`".join([str(i) for i in movies_df.columns.tolist()])

    for i, row in movies_df.iterrows():
        sql = "INSERT INTO `Estadisticas` (`" + cols + "`) VALUES (" + "%s," * (len(row) - 1) + "%s)"
        cursor.execute(sql, tuple(row))
        conn.commit()

    conn.close()


# lambada 1 handler
movies_json = json.loads(Extract_json_from_S3('produccion'))
##invokelambda(movies_json,'fliter_data_movies')
# lambda 2 handler
movie_df = filter_json_info(movies_json)
movies_json_df = movie_df.to_json(orient='split')
##invokelambda(movies_json_df,'')

# lammbda 3 handler informacion con el evento
jsond = json.loads(jsond)
movies_df2 = pd.DataFrame(jsond['data'], columns = jsond['columns'])

endpoint = "databasemovies.cnjxvyvv4pkm.us-east-2.rds.amazonaws.com"
PORT = "3306"
username = "admin"
password = "12345678"
databsa_name = "databasemovies"

conn = pymysql.connect(endpoint, user=username, passwd=password)

cursor = conn.cursor()







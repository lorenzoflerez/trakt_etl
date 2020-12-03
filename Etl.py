import boto3
import pandas as pd
import json

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
    api_download =json['api_download']
    for i in range(len(movies_json)):
        movie_info = movies_json[i]['list_info']['movies_summary']
        movies_info_df = filter_info_movies(movie_info,api_download)
        movies_info_df =movies_info_df.append(movies_info_df)
    return movies_info_df

#download_api : momento en el que se baja la informacion de la api
def filter_info_movies(movies_info,download_api):
    movies_info_df = pd.DataFrame(
        columns=('title', 'year', 'id_movie', 'overview', 'released', 'country', 'language', 'genres'))

    movies_stas_df = pd.DataFrame(
        columns=('runtime', 'rating', 'id_movie', 'votes', 'comment_count', 'updated_at','translated','download_api'))

    for j in range(len(movies_info)):
        summary = movies_info[j]

        movies_info_df = pd.DataFrame(
            [[summary['title'], summary['year'], summary['ids']['trakt'], summary['overview'],
              summary['released'], summary['country'], summary['language'], summary['genres']]],
            columns=['title', 'year', 'id_movie', 'overview', 'released', 'country', 'language', 'genres']).append(
            movies_info_df)

        movies_stas_df = pd.DataFrame(
            [[summary['runtime'], summary['rating'], summary['ids']['trakt'],
              summary['votes'],summary['comment_count'], summary['updated_at'],summary['available_translations'],download_api]],
             columns =['runtime', 'rating', 'id_movie', 'votes', 'comment_count', 'updated_at','translated','download_api']).append(
            movies_stas_df)

    movies_df = pd.merge(movies_info_df, movies_stas_df, on='id_movie')
    return movies_df


def change_type_data(movies_df):
    ## hacer los procesos de cambiar los tipos de datos
    d=''
def update_info_bd(movies_df):
    ## Lo necesario para conectarse a RBs
    d=''
#lambada 1 handler
movies_json = json.loads(Extract_json_from_S3('produccion'))
##invokelambda(movies_json,'')
#lambda 2 handler
movie_df = filter_json_info(movies_json)
movies_json_df = movie_df.to_json(orient='split')
##invokelambda(movies_json_df,'')

#lammbda 3 handler informacion con el evento
jsond = json.loads(jsond)
movies_df2 = pd.DataFrame(jsond['data'], columns = jsond['columns'])




# rint(movies_df.astype(str).dtypes)
# print(movies_df['updated_at'].dtype)

##movies_df['updated_at'] = pd.to_datetime(movies_df['updated_at'])

##print(movies_df['updated_at'].dtype)

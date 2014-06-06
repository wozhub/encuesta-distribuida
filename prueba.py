#!/usr/bin/python

import base64 #para encodear la subida de surveys
from libreria import *

mykey=get_session_key()

if mykey is not None:
    print "Obtuve",mykey

    #prueba import_survey
    """Creamos una nueva encuesta a partir de un archivo"""
    with open('./limesurvey_survey_465943.lss', 'rb') as f:
        encoded_string = base64.b64encode(f.read())
    sid = import_survey(mykey,encoded_string,"prueba",465000)
    activada = activate_survey(mykey,sid)

    #prueba exportacion de respuestas
    """La respuestas se descargan de un archivo csv"""
    datos=export_responses(mykey,465943)
    decoded_string = base64.b64decode(datos)
    with open('salida.csv', 'wb') as f:
        print decoded_string
        f.write(decoded_string)

    #prueba import
    """Iteramos sobre un archivo para cargar las respuestas"""
    importar_desde_archivo(mykey,sid,'salida.csv')

    release_session_key(mykey)

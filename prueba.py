#!/usr/bin/python

import base64 #para encodear la subida de surveys
import csv

from json import dumps

from libreria import *


mykey=get_session_key()

#print export_responses2(mykey,'566237').decode('base64')
#get_question_properties(mykey,'574')

if mykey is not None:
    print "Obtuve",mykey

    #prueba import_survey
    #with open('./limesurvey_survey_465943.lss', 'rb') as f:
    #    encoded_string = base64.b64encode(f.read())

    #import_survey(mykey,datos,"prueba",465000)

    #prueba export
    #datos=export_responses(mykey,46593)
    #decoded_string = base64.b64decode(datos)
    #with open('salida.csv', 'wb') as f:
    #    f.write(decoded_string)

    #prueba import
    importar_desde_archivo(mykey,465000,'salida.csv')


    release_session_key(mykey)

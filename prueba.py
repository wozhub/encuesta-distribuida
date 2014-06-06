#!/usr/bin/python

import base64 #para encodear la subida de surveys
from libreria import *


mykey=get_session_key()

#print export_responses2(mykey,'566237').decode('base64')
#get_question_properties(mykey,'574')

if mykey is not None:
    print "Obtuve",mykey

    with open('./limesurvey_survey_465943.lss', 'rb') as f:
        encoded_string = base64.b64encode(f.read())

    print import_survey(mykey,datos,"prueba",465000)

    release_session_key(mykey)

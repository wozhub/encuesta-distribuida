#!/usr/bin/python

from requests import session
from time import sleep

usuario = 'kadmin**'
clave = '&E#&&W&O$B'

urlLogin = "http://encuestas.proyectokoala.org/index.php/admin/authentication/sa/login"
urlDescarga = "http://encuestas.proyectokoala.org/index.php/admin/export/sa/survey/action/exportstructurexml/surveyid/343458"


payload = { 'action': '/index.php/admin/authentication/sa/login',
            'user': usuario,
            'password': clave }

with session() as c:
    c.post(urlLogin, data=payload)
    request = c.get(urlDescarga)


    print request.headers
    sleep(5)

    f = open('salida', 'wb')

    for chunk in request.iter_content(chunk_size=512 * 1024):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
            f.close()

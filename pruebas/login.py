#!/usr/bin/python

import urllib, urllib2, cookielib

usuario = 'kadmin**'
clave = '&E#&&W&O$B'

urlLogin = "http://encuestas.proyectokoala.org/index.php/admin/authentication/sa/login"
urlDescarga = "http://encuestas.proyectokoala.org/index.php/admin/export/sa/survey/action/exportstructurexml/surveyid/343458"

cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

login_data = urllib.urlencode({'user' : usuario, 'password' : clave})

opener.open(urlLogin, login_data)

resp = opener.open(urlDescarga)
print resp.read()

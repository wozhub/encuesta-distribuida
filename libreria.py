#!/usr/bin/python

import urllib2
import json
import sys
from csv import DictReader

import base64 #para encodear la subida de surveys

from credenciales import usuario,clave,urlBase


def _generarRequest(url,data):
    print data
    req = urllib2.Request(url=urlBase,data=data)
    req.add_header('content-type', 'application/json')
    req.add_header('connection', 'Keep-Alive')
    return req


def list_surveys(session_key):
    json_list_surveys = _list_surveys(session_key)

    encuestas=[]
    for e in json_list_surveys:
        encuesta=e['sid'],e['surveyls_title'] # Me quedo con el SID y el Titulo
        encuestas.append(encuesta)

    return encuestas


def _list_surveys(session_key):
    """Devuelve el JSON ENTERO"""
    data = """{ "id": 1,
                "method": "list_surveys",
                "params": { "sSessionKey": "%s" } }""" % (session_key)

    req = _generarRequest(urlBase,data)

    try:
        f = urllib2.urlopen(req)
        myretun = f.read()
        j=json.loads(myretun)
        return j['result']

    except:
        e = sys.exc_info()[0]
        print ( "<p>Error: %s</p>" % e )


def import_survey(session_key,datos,titulo,sid):
    data = """{ "id": 1,
                "method": "import_survey",
                "params": { "sSessionKey": "%s",
                            "sImportData": "%s",
                            "sImportDataType": "lss",
                            "sNewSurveyName": "%s",
                            "DestSurveyID": %d } }""" % (session_key, datos, titulo, sid)

    req = _generarRequest(urlBase,data)

    try:
        f = urllib2.urlopen(req)
        myretun = f.read()
        j=json.loads(myretun)
        return j['result']

    except:
        e = sys.exc_info()[0]
        print ( "<p>Error: %s</p>" % e )


def get_session_key():
    data="""{   "id": 1,
                "method": "get_session_key",
                "params": { "username": "%s",
                            "password": "%s" } } """ % (usuario, clave)

    req = _generarRequest(urlBase,data)

    try:
        f = urllib2.urlopen(req)
        myretun = f.read()
        j=json.loads(myretun)
        return j['result']
    except:
        e = sys.exc_info()[0]
        print ( "<p>Error: %s</p>" % e )


def release_session_key(relkey):
    req = urllib2.Request(url=urlBase,\
                          data='{\"method\":\"release_session_key\",\"params\":{\"sSessionKey\":\"'+relkey+'\"},\"id\":1}')
    req.add_header('content-type', 'application/json')
    req.add_header('connection', 'Keep-Alive')
    try:
        f = urllib2.urlopen(req)
        myretun = f.read()
        #print myretun
        j=json.loads(myretun)
        return j['result']
    except :
        e = sys.exc_info()[0]
        print ( "<p>Error: %s</p>" % e )


def export_responses(session_key,sid):
    data=""" {          "method":"export_responses",
                        "params": { "sSessionKey": "%s",
                                    "iSurveyID":  %d,
                                    "DocumentType": "csv",
                                    "sLanguageCode": "de",
                                    "sHeadingType": "full" },
                        "id": 1 } """ % (session_key,sid)

    req = _generarRequest(urlBase,data)

    try:
        f = urllib2.urlopen(req)
        myretun = f.read()
        j=json.loads(myretun)
        return j['result']
    except :
        e = sys.exc_info()[0]
        print ( "<p>Error: %s</p>" % e )

def importar_desde_archivo(session_key,sid,archivo):
    respuestas = DictReader(open(archivo))

    for r in respuestas:
        print json.dumps(r)

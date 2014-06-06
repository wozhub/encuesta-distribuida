#!/usr/bin/python

import urllib2
import json
import sys
from csv import DictReader

from credenciales import usuario,clave,urlBase

def _obtenerJson(url,data):
    #print data
    req = urllib2.Request(url=url,data=data)
    req.add_header('content-type', 'application/json')
    req.add_header('connection', 'Keep-Alive')

    try:
        f = urllib2.urlopen(req)
        myretun = f.read()
        return json.loads(myretun)

    except:
        e = sys.exc_info()[0]
        print ( "<p>Error: %s</p>" % e )


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

    return _obtenerJson(urlBase,data)['result']


def activate_survey(session_key,sid):
    data = """{ "id": 1,
                "method": "activate_survey",
                "params": { "sSessionKey": "%s",
                            "SurveyID": %d } }""" % (session_key,sid)
    return _obtenerJson(urlBase,data)['result']


def import_survey(session_key,datos,titulo,sid):
    data = """{ "id": 1,
                "method": "import_survey",
                "params": { "sSessionKey": "%s",
                            "sImportData": "%s",
                            "sImportDataType": "lss",
                            "sNewSurveyName": "%s",
                            "DestSurveyID": %d } }""" % (session_key, datos, titulo, sid)
    return _obtenerJson(urlBase,data)['result']


def get_session_key():
    data="""{   "id": 1,
                "method": "get_session_key",
                "params": { "username": "%s",
                            "password": "%s" } } """ % (usuario, clave)
    return _obtenerJson(urlBase,data)['result']


def release_session_key(session_key):
    data = """ { "method": "release_session_key",
                 "params": { "sSessionKey" : "%s"},
                 "id":1}' }""" % (session_key)
    return _obtenerJson(urlBase,data)['result']


def export_responses(session_key,sid):
    data=""" {          "method":"export_responses",
                        "params": { "sSessionKey": "%s",
                                    "iSurveyID":  %d,
                                    "DocumentType": "csv",
                                    "ResponseType": "long",
                                    "sHeadingType": "full" },
                        "id": 1 } """ % (session_key,sid)
    return _obtenerJson(urlBase,data)['result']


def _add_response(session_key,sid,datos):
    data=""" {          "method":"add_response",
                        "params": { "sSessionKey": "%s",
                                    "iSurveyID": %d,
                                    "aResponseData": %s },
                        "id": 1 } """ % (session_key,sid,datos)
    return _obtenerJson(urlBase,data)['result']


def importar_desde_archivo(session_key,sid,archivo):
    respuestas = DictReader(open(archivo))

    for r in respuestas:
        _add_response(session_key,sid,json.dumps(r))


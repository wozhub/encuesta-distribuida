#!/usr/bin/python

from libreria import *
session_key=get_session_key()

if session_key is not None:
    print "Obtuve",session_key

    for encuesta in list_surveys(session_key):
        print encuesta

    release_session_key(session_key)

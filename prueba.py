import urllib
import urllib2
import json
import sys
# There is an generic json-rpc implemantation in Python but it dose not work for me in this case so I worte Some functions


       
def get_session_key():
    req = urllib2.Request(url='http://myurl/index.php/admin/remotecontrol',\
                          data='{\"method\":\"get_session_key\",\"params\":{\"username\":\"admin\",\"password\":\"mypassword\"},\"id\":1}')
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
               
def get_question_properties(skey,QuestionID):
    req = urllib2.Request(url='http://myurl/index.php/admin/remotecontrol',\
                          data='{\"method\":\"get_question_properties\",\"params\":{\"sSessionKey\":\"'+skey+'\",\"iQuestionID\":'+QuestionID+',\
\"aQuestionSettings\":[\"gid\",\"type\",\"help\",\"language\",\"sid\",\"question_order\",\"question\",\"subquestions\"]},\"id\": 1}')

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

               
def release_session_key(relkey):
    req = urllib2.Request(url='http://myurl/index.php/admin/remotecontrol',\
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


def export_responses2(skey,sid):
    req = urllib2.Request(url='http://myurl/index.php/admin/remotecontrol',\
                          data='{\"method\":\"export_responses\",\"params\":{\"sSessionKey\":\"'+skey+'\",\"iSurveyID\":\"'+sid+'\",\
\"DocumentType\":\"csv\",\"sLanguageCode\":\"de\",\"sHeadingType\":\"full\"},\
"id\": 1}')
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

               
mykey=get_session_key()
print export_responses2(mykey,'566237').decode('base64')
get_question_properties(mykey,'574')
print release_session_key(mykey)

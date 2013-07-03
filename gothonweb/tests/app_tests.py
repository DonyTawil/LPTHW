#This code once run shouldn't get any errors but when it would it would have the lines that are preceded by##
from nose.tools import *
from bin.app import session
from bin.app import app
from tests.tools import assert_response # a special function that studies resp assert_response(response, status ,contains,headers,match)
from gothonweb.map import code,c #import the cheat codes
import web
import base64
import pickle


  
#test from laser_weapon_armory to bridge
def test__start__end():
    resp=app.request("/game")
    data={"action":"tell a joke"}
    resp=app.request("/game",method="POST",data=data)
    x=((resp.headers['Set-Cookie']).split(";")[0])
    x=x.lstrip('webpy_session_id=')
    y=(open('docs/sessions/%s'%x).read())
    store=web.session.DiskStore('docs/sessions')
    print(store.decode(y))
    #assert_response(resp,status="300")
 
  
    
    
        

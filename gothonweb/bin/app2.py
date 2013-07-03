import web
from gothonweb import map
from gothonweb import maptext

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
    '/signup',"Signup",
    "/signin","Signin"
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")


if web.config.get('_session') is None:
    store = web.session.DiskStore('docs/sessions')
    session = web.session.Session(app, store, initializer={'room': None,'count':0,'name':None})#each time I add a dict object I have to delete all the sessions
    web.config._session = session
else:
    session = web.config._session



class Index(object):
    def GET(self):
        session.room = map.START
        session.name = map.START.name
        maptext.lwa_tries=0
        session.count=0
        web.seeother("/game")
        

       
class GameEngine(object):
    
    def GET(self):
                     
        session.count+=1
        tries=10
        if session.room:
            session.name=session.room.name
            maptext.cumulative_score+=session.room.score #To add score
            if session.room.ide == 2:##At laser weapon armory
                if maptext.lwa_tries==0:
                    maptext.lwa_tries=session.count#set up counter  ##
                elif session.count>maptext.lwa_tries+10:
                    session.room=session.room.go('*')    
                else:
                    tries+=maptext.lwa_tries-session.count
                    session.name=session.room.name
                    return render.show_room(room=session.room,tries=tries)    
            return render.show_room(room=session.room,tries=None)
        else:  #In case there are no sessions stored and you go to /game before going to / to set up init values
            return render.you_died()

    def POST(self):
        form = web.input(action="")                              
        if session.room and session.room.go(form.action):
            session.room = session.room.go(form.action)
        elif ((session.room == map.laser_weapon_armory) or (session.room == map.laser_weapon_armoryc)):
            lwa_tries+=1

        
        web.seeother("/game")


class Signup(object):
    def GET(self):
        return render.signup()

    def POST(self):
        form=web.input()
        name="%s"%form.name
        score="0" #The initial score of the signed up player
        web.setcookie('%r'%name,score,3600)#Check to see if int is accepted or just string        
        if session.name == None:#just in case didn't pass by '/' to make session equal to map.start
            web.seeother('/')
        else:                    
            web.seeother('/game')



class Signin(object):
    def GET(self):
        return render.signin(name=None)

    def POST(self):   
        form=web.input()
        name="%r"%form.name
        cookie=web.cookies().get(name) #Get None if cookie is not present
        if cookie:
                web.setcookie(name,cookie,36000) # To reset expiry date
                if session.name==None:
                    return web.seeother('/')
                else:
                    return web.seeother('/game')    
        else:
            return render.signin(name=False)

        

if __name__== "__main__":
    app.run()                                     

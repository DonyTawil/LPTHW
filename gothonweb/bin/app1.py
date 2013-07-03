import web
from gothonweb import map

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
    '/signup',"Signup",
    "/signin","Signin"
    
    
)


cumulative_score=0 #The score that the player has accumulated during the game
app = web.application(urls, globals())


if web.config.get('_session') is None:
    store = web.session.DiskStore('docs/sessions')
    session = web.session.Session(app, store, initializer={'room': None,'count':0,'name':None})#each time I add a dict object I have to delete all the sessions
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


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
        print(cookie)
        if cookie:
                web.setcookie(name,cookie,36000) # To reset expiry date
                if session.name==None: 
                    return web.seeother('/')
                else:
                    return web.seeother('/game')    
        else:
            return render.signin(name=False)            
                


class Index(object):

    def GET(self):
        #From docu: this is used to "setup" the session with starting values
        session.room = map.START
        session.name = map.START.name
        map.c=0
        session.count=0
        web.seeother("/game")
        

       
class GameEngine(object):
    
    def GET(self):
                     
        session.count+=1
        tries=10
        if (session.room and session.room.ide == 1 and map.c==0):
            map.c=session.count#set up counter
            
            
        if (session.count>map.c+10 and session.room.ide==1):#when at laser weapon armory
            session.room=session.room.go('*')        
        
        if session.room and session.room.ide ==1:
            tries+=map.c-session.count
            session.name=session.room.name
           
            return render.show_room(room=session.room,tries=tries)

        if session.room:
            session.name=session.room.name
            cumulative_score+=session.room.score #To add score
            
            return render.show_room(room=session.room,tries=None)

        else:
            #In case there are no sessions stored and you go to /game before going to / to set up init values
            return render.you_died()

    def POST(self):

        form = web.input(action="")                               
        
        
        if session.room and session.room.go(form.action):
            session.room = session.room.go(form.action)
            
            
        elif ((session.room == map.laser_weapon_armory) or (session.room == map.laser_weapon_armoryc)):
            session_counter+=1

        
        web.seeother("/game")

if __name__== "__main__":
    app.run()                                     

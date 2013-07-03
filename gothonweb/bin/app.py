import web
from gothonweb import map as map1
from gothonweb import map02 as map2
from gothonweb import maptext
from gothonweb import lexicon
from gothonweb import parse

the_map=map2

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
    '/signup',"Signup",
    "/signin","Signin",
    "/just_help","TheHelp",
    "/save","Save"
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
    def GET(self):#initializers
        session.room = the_map.START
        session.name = the_map.START.name
        maptext.lwa_tries=0
        maptext.save=True
        maptext.help=False
        session.count=0
        web.seeother("/game")
        

       
class GameEngine(object):
    
    def GET(self):             
        session.count+=1
        tries=10
        if session.room:
            session.name=session.room.name
            maptext.cumulative_score+=session.room.score #To add score
            if session.room.ide == 2 and the_map==map1:#At laser weapon armory in map1
                if maptext.lwa_tries==0:
                    maptext.lwa_tries=session.count#set up counter  
                elif session.count>maptext.lwa_tries+10:
                    session.room=session.room.go('*')    
                else:
                    tries+=maptext.lwa_tries-session.count
                    session.name=session.room.name
                    return render.show_room(room=session.room,tries=tries,help=maptext.help,save=maptext.save)    
            return render.show_room(room=session.room,tries=tries,help=maptext.help,save=maptext.save)
        else:  #In case there are no sessions stored and you go to /game before going to / to set up init values
            return render.you_died()

    def POST(self):
        save=True#To reset save variable in case player saved and yet he was not signed in
        form = web.input(action="")
        if the_map==map1:                              
            if session.room and session.room.go(form.action):
                if session.room.ide!=session.room.go(form.action).ide:#To check if still in the same room to keep the help
                    maptext.help=False
                session.room = session.room.go(form.action)
            elif ((session.room == map.laser_weapon_armory) or (session.room == map.laser_weapon_armoryc)):
                lwa_tries+=1
        elif the_map==map2:
            if session.room:
                Scanner=lexicon.Lexicon()
                player_input=Scanner.scan(form.action)
                player_input=parse.Sentence.parse_sentence(player_input)
                final_input=player_input.subject+" "+player_input.verb+" "+player_input.object
                if player_input.num:
                    final_input+=" "+player_input.num  
                session.room.go(final_input)
                session.room=map2.Player.room       #Session.room.go(...) Modifies the Player.room at map2 so i reset session.room to the new value of Player.room
        
        web.seeother("/game")


class Signup(object):
    def GET(self):
        return render.signup()

    def POST(self):
        form=web.input()
        name="%s"%form.name
        score={'score':maptext.cumulative_score} #The initial score of the signed up player
        web.setcookie('%r'%name,score,3600)       
        if session.name == None:#just in case didn't pass by '/' to make session equal to map.start
            web.seeother('/')
        else:                    
            web.seeother('/game')



class Signin(object):
    @classmethod
    def __init__(self):
        cls.name=None#so we can access the name of the user in save
        
    def GET(self):
        return render.signin(name=None)

    def POST(self):   
        form=web.input()
        name="%r"%form.name
        cookie=web.cookies().get(name) #Get None if cookie is not present
        if cookie:
                cls.name=name
                maptext.signed=True
                web.setcookie(name,cookie,36000) # To reset expiry date
                if session.name==None:
                    return web.seeother('/')
                else:
                    return web.seeother('/game')    
        else:
            return render.signin(name=False)

class TheHelp(object):#This is an html link to activate help
    def GET(self):
        maptext.help=True#turn on help
        print(help)
        web.seeother("/game")

class Save(object):#Save progress
    def GET(self):
        if maptext.signed:
            cookie=web.cookies().get(Signin.name)
            if cookie<cumulative_score:#To save high score
                web.setcookie(Signin.name,cumulative_score,3600)
            else:
                web.setcookie(Signin.name,cookie,3600)    
            web.seeother("/game")
        else:
            maptext.save=False
            web.seeother("/game")    
                    

        

if __name__== "__main__":
    print("app.run()")
    app.run()                                     

from gothonweb.map2text import*
from random import randint
#New map where I want the player to be able to fight enemies
#for objects can create list



class Player(object):
    inventory={}
    health=100
    room=None#so that add paths etc can change it
    does_not_compute=False

    def __init__(self):
        pass

    @classmethod
    def reduce_health(self,num):
        Player.health-=num
        if Player.health <= 0:
            Player.room=Death_Room    
                     

class Enemy(object):
    def __init__(self,name,health,attack,death=None):
        self.health=health
        self.name=name
        self.attack=attack
        self.death=death #string describing death

    def attack_enemy(self):
        return (self.name,-10)#Name of enemy,damage to enemy

    def enemy_attack_player(self):
        a=randint(-20,20)
        the_attack=(self.attack/2 + (self.attack/2)*(float(a)/20))
        Player.health-=the_attack    
        
            

class RoomWar(object):
    def __init__(self,description,name,ide=None,objects=None,the_changes={},score=5,help=None):#same stuff
        self.description=str(description)
        self.primary_description=self.description 
        self.name=name
        self.help=help
        self.score=score
        self.ide=ide
        self.objects={}#dicts to hold various things like objects that are in the room (gun),or actions like examine
        self.enemies={}#dict to hold enemies
        self.paths={}#dict to hold places u can go to 
         
    def add_enemy(self,name,health,attack,death=None):
        name=str(name)
        self.enemies.update({name:Enemy(name,health,attack,death)})       

    def take_objects(self,stuff):
        if stuff in self.objects: #and stuff not in Player.inventory:
            out=self.objects.get(stuff)
            return (out,stuff)
        
                
    def add_objects(self,objects):
        self.objects.update(objects)

    def add_paths(self,paths):        
        self.paths.update(paths) 

    def enemies_turn(self):
            for i in self.enemies:
                self.enemies[i].enemy_attack_player()
     
    def go(self,action):#Have to nosetest it
        does_not_compute=False
        a=self.paths.get(action,None)
        if (a!=None):#test if path exist
            if type(a)!= type(RoomWar('class to give type','test')):#Test if dealing with RoomWar instance
                if type(a[0])==type(str()): #If not dealing with RoomWar test if dealing with a take_objects' return or enemy thing
                    if type(a[1])==type(str()):#dealing with objects
                        self.description=a[0]
                        self.objects.__delitem__(a[1])#delete the object because player shouldn't be able to use it twice
                    elif type(a[1])==type(int()):#if Dealing with enemies
                        self.enemies[a[0]].health+=a[1]
                        if self.enemies[a[0]].health <=0:
                            self.description=self.enemies[a[0]].death
                            self.enemies.__delitem__(a[0])
                self.primary_description=self.description #To store new description about the room 
                if self.enemies!={}:            
                    self.enemies_turn()
                    self.description+="\nThe enemies have attacked you and reduced your health to %d"%Player.health
                                      
            else: #=dealing with a RoomWar instance 
                if self.enemies != {}:
                    self.description+=" there are still enemies in the room can't do that!!"  
                elif self.objects !={}:
                    self.description+=" You still need to use some objects in the area!!"
                if self.enemies=={} and self.objects=={}:                  
                    Player.room=a
        else:
            does_not_compute=True
            self.description=self.primary_description   
               
      

#Will change them soon
SpaceShip=RoomWar(ss,'Space ship')
SpaceShip.add_objects({'keypad':'''after taking your special forces mask you use the keypad to open the door
leading outside. You take a quick peek and make sure the coast 
is clear. Your mission is to recon mars and make contact with 
the alien race.Assume it is hostile!! But do not engage unless 
engaged upon'''})
Death_Room=RoomWar('U are dead','death room')
Outside=RoomWar(out,'elsewhere')
SpaceShip.add_paths({'player go out':Outside})

Player.room=SpaceShip
START=Player.room
def Game_engine():  
    while(True):
        print(Player.room.description)
        action=raw_input('>')
        Player.room.go(action)
        

#Game_engine()                       







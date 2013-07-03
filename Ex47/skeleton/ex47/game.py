from random import randint

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.health=100
        self.e=False
        self.enemy=None
    def go(self, direction):
        a=self.paths.get(direction, None)
        if ((a!= None)and(self.e==False)):
            return a
        else:
            print("can't go there")    
            return "can't go there"
    def add_paths(self, paths):
        self.paths.update(paths)

    def add_enemy(self,desc):
        self.e=True
        self.description+='\n'+desc        
        self.enemy=Enemy()

class Enemy(object):
    def __init__(self):
        self.health=100


    def attack(self):
        chance=randint(1,+50)
        self.health-=chance
        
#a=Room('Test_room','Your are in a testing room that does nothing')
#north=Room('tnorth','You are in test room north')
#south=Room('tsouth','you are in test room south') 
#a.add_paths({'north':north,'south':south})
                   
